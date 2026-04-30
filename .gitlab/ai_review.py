#!/usr/bin/env python3
"""
AI-powered documentation review using Claude API + Vale linter.
Runs Vale on changed Markdown files, sends findings + content to Claude,
and posts GitLab *suggestions* (apply-with-one-click) on specific diff lines.

Required CI/CD variables:
  - ANTHROPIC_API_KEY: Claude API key
  - CI_MERGE_REQUEST_IID: MR ID (auto-set by GitLab)
  - CI_PROJECT_ID: Project ID (auto-set by GitLab)
  - CI_API_V4_URL: GitLab API URL (auto-set by GitLab)
  - GITLAB_TOKEN: GitLab API token with comment permissions
  - CI_MERGE_REQUEST_DIFF_BASE_SHA: Base commit (auto-set by GitLab)
  - CI_COMMIT_SHA: Head commit (auto-set by GitLab)

Optional:
  - VALE_PATH: Path to vale binary (default: /tmp/vale/vale)
"""

import json
import os
import subprocess
import sys
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("ERROR: anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)

try:
    import requests
except ImportError:
    print("ERROR: requests package not installed. Run: pip install requests")
    sys.exit(1)

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
GITLAB_TOKEN = os.environ.get("GITLAB_TOKEN")
CI_API_V4_URL = os.environ.get("CI_API_V4_URL", "https://gitlab.com/api/v4")
CI_PROJECT_ID = os.environ.get("CI_PROJECT_ID")
CI_MERGE_REQUEST_IID = os.environ.get("CI_MERGE_REQUEST_IID")
CI_MERGE_REQUEST_DIFF_BASE_SHA = os.environ.get("CI_MERGE_REQUEST_DIFF_BASE_SHA")
CI_COMMIT_SHA = os.environ.get("CI_COMMIT_SHA")
VALE_PATH = os.environ.get("VALE_PATH", "/tmp/vale/vale")

REVIEW_PROMPT = """\
You are a technical documentation editor. Review the Markdown file below \
and suggest line-level improvements for clarity and readability.

A linter (Vale) has already flagged specific issues — listed under "Vale findings". \
Use them as a starting point but also find issues the linter missed.

Focus on:
1. Sentences over 25 words — suggest shorter alternatives.
2. Passive voice — rewrite in active voice.
3. Complex words — suggest simpler synonyms (e.g., "utilize" → "use").
4. Weak openings — rewrite "There is/are..." constructions.
5. Filler words — remove "basically", "obviously", "actually", etc.
6. Clarity — fix ambiguous or vague statements.

Rules:
- Only suggest changes that improve readability WITHOUT changing technical meaning.
- Do NOT suggest changes to code blocks, YAML frontmatter, URLs, or image references.
- Each suggestion must target a SINGLE line (or a small range of consecutive lines).
- Provide the COMPLETE replacement for the line(s) — not partial edits.
- Maximum 15 suggestions per file.

CRITICAL: Respond with ONLY a JSON array. No other text. Each element:
{{
  "start_line": <first line number to replace (1-indexed)>,
  "end_line": <last line number to replace (1-indexed, same as start_line for single line)>,
  "replacement": "<the full replacement text for these lines>",
  "reason": "<brief reason>"
}}

If no improvements needed, respond with: []

---

File: {filename}

### Vale findings

{vale_output}

### File content (with line numbers)

{content}
"""

MAX_FILE_SIZE = 12000  # characters — leave room for Vale output in token budget

HEADERS = {"PRIVATE-TOKEN": GITLAB_TOKEN}


def get_head_sha():
    """Get HEAD commit SHA."""
    if CI_COMMIT_SHA:
        return CI_COMMIT_SHA
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True
    )
    return result.stdout.strip()


def get_changed_files():
    """Get list of changed .md files in the current MR."""
    base_sha = CI_MERGE_REQUEST_DIFF_BASE_SHA
    if not base_sha:
        print("WARNING: CI_MERGE_REQUEST_DIFF_BASE_SHA not set — falling back to git fetch.")
        target_branch = os.environ.get("CI_MERGE_REQUEST_TARGET_BRANCH_NAME", "main")
        subprocess.run(
            ["git", "fetch", "origin", target_branch, "--depth=50"],
            capture_output=True,
        )
        base_sha = f"origin/{target_branch}"

    diff_cmd = ["git", "diff", "--name-only", "--diff-filter=ACMR", base_sha, "HEAD"]
    print(f"Running: {' '.join(diff_cmd)}")
    try:
        result = subprocess.run(
            diff_cmd, capture_output=True, text=True, check=True
        )
        print(f"git diff stdout: {result.stdout!r}")
        files = [
            f.strip()
            for f in result.stdout.strip().split("\n")
            if f.strip().endswith(".md")
            and "release_notes_low-level" not in f
            and "previous_releases" not in f
        ]
        return files
    except subprocess.CalledProcessError as e:
        print(f"WARNING: git diff failed (exit {e.returncode}): {e}")
        print(f"  stdout: {e.stdout}")
        print(f"  stderr: {e.stderr}")
        return []


def get_changed_lines(filepath):
    """Get set of line numbers that were added/modified in the diff."""
    base_sha = CI_MERGE_REQUEST_DIFF_BASE_SHA or "HEAD~1"
    try:
        result = subprocess.run(
            ["git", "diff", "-U0", base_sha, "HEAD", "--", filepath],
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError:
        return set()

    changed = set()
    for line in result.stdout.split("\n"):
        # Parse unified diff hunk headers: @@ -old,count +new,count @@
        if line.startswith("@@"):
            parts = line.split("+")
            if len(parts) >= 2:
                range_part = parts[1].split("@@")[0].strip()
                if "," in range_part:
                    start, count = range_part.split(",")
                    start, count = int(start), int(count)
                else:
                    start, count = int(range_part), 1
                for i in range(start, start + count):
                    changed.add(i)
    return changed


def run_vale(filepath):
    """Run Vale on a single file and return its output."""
    try:
        result = subprocess.run(
            [VALE_PATH, filepath], capture_output=True, text=True
        )
        output = result.stdout.strip()
        return output if output else "No issues found."
    except FileNotFoundError:
        print(f"WARNING: Vale not found at {VALE_PATH}")
        return "Vale not available — skipped."


def review_file(client, filepath, vale_output):
    """Send file content + Vale findings to Claude, get JSON suggestions."""
    try:
        lines = Path(filepath).read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        return []

    if len(lines) < 3:
        return []

    # Add line numbers for Claude
    numbered = "\n".join(f"{i+1:4d} | {line}" for i, line in enumerate(lines))
    if len(numbered) > MAX_FILE_SIZE:
        numbered = numbered[:MAX_FILE_SIZE] + "\n...[truncated]..."

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        messages=[
            {
                "role": "user",
                "content": REVIEW_PROMPT.format(
                    filename=filepath,
                    vale_output=vale_output,
                    content=numbered,
                ),
            }
        ],
    )

    raw = message.content[0].text.strip()
    # Strip markdown code fences if present
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1] if "\n" in raw else raw[3:]
    if raw.endswith("```"):
        raw = raw[: raw.rfind("```")]

    try:
        suggestions = json.loads(raw)
        if not isinstance(suggestions, list):
            print(f"WARNING: Claude returned non-list: {raw[:200]}")
            return []
        return suggestions
    except json.JSONDecodeError as e:
        print(f"WARNING: Failed to parse Claude response as JSON: {e}")
        print(f"  Raw response: {raw[:500]}")
        return []


def post_suggestion(filepath, start_line, end_line, replacement, reason, base_sha, head_sha):
    """Post a GitLab suggestion comment on specific diff lines."""
    if not all([GITLAB_TOKEN, CI_PROJECT_ID, CI_MERGE_REQUEST_IID]):
        print(f"  [dry-run] L{start_line}-{end_line}: {reason}")
        print(f"            → {replacement[:100]}")
        return True

    url = (
        f"{CI_API_V4_URL}/projects/{CI_PROJECT_ID}"
        f"/merge_requests/{CI_MERGE_REQUEST_IID}/discussions"
    )

    # Build the suggestion body — GitLab syntax
    # For multi-line: ```suggestion:-N+0  where N = lines before the anchor line
    lines_before = end_line - start_line  # anchor is end_line
    suggestion_block = f"```suggestion:-{lines_before}+0\n{replacement}\n```"
    body = f"**AI Review** — {reason}\n\n{suggestion_block}"

    payload = {
        "body": body,
        "position": {
            "base_sha": base_sha,
            "start_sha": base_sha,
            "head_sha": head_sha,
            "position_type": "text",
            "old_path": filepath,
            "new_path": filepath,
            "new_line": end_line,
        },
    }

    resp = requests.post(url, headers=HEADERS, json=payload, timeout=30)
    if resp.status_code in (200, 201):
        print(f"  Posted suggestion on L{start_line}-{end_line}: {reason}")
        return True
    else:
        print(f"  FAILED suggestion on L{start_line}-{end_line}: {resp.status_code}")
        print(f"    Response: {resp.text[:300]}")
        return False


def main():
    # Skip if this commit is from applying a GitLab suggestion
    # (prevents infinite loop: suggestion → apply → commit → pipeline → suggestion)
    commit_title = os.environ.get("CI_COMMIT_TITLE", "")
    if "Apply suggestion" in commit_title or "Apply 1 suggestion" in commit_title:
        print(f"Skipping: commit is from applying a suggestion ({commit_title!r}).")
        return

    if not ANTHROPIC_API_KEY:
        print("ERROR: ANTHROPIC_API_KEY not set.")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    changed_files = get_changed_files()
    if not changed_files:
        print("No changed Markdown files to review.")
        return

    base_sha = CI_MERGE_REQUEST_DIFF_BASE_SHA or "unknown"
    head_sha = get_head_sha()
    print(f"Base SHA: {base_sha}")
    print(f"Head SHA: {head_sha}")
    print(f"Reviewing {len(changed_files)} file(s)...")

    total_posted = 0
    total_skipped = 0

    for filepath in changed_files:
        print(f"\n  Reviewing: {filepath}")

        # Get lines that actually changed in the diff
        changed_lines = get_changed_lines(filepath)
        if not changed_lines:
            print(f"  No changed lines detected in diff — skipping.")
            continue
        print(f"  Changed lines: {sorted(changed_lines)[:20]}{'...' if len(changed_lines) > 20 else ''}")

        vale_output = run_vale(filepath)
        suggestions = review_file(client, filepath, vale_output)

        if not suggestions:
            print(f"  No suggestions for {filepath}.")
            continue

        print(f"  Claude returned {len(suggestions)} suggestion(s).")

        for s in suggestions:
            start = s.get("start_line", 0)
            end = s.get("end_line", start)
            replacement = s.get("replacement", "")
            reason = s.get("reason", "Readability improvement")

            # Only post suggestions on lines that are in the diff
            suggestion_lines = set(range(start, end + 1))
            if not suggestion_lines & changed_lines:
                print(f"  Skipping L{start}-{end}: not in diff")
                total_skipped += 1
                continue

            ok = post_suggestion(filepath, start, end, replacement, reason, base_sha, head_sha)
            if ok:
                total_posted += 1

    print(f"\nDone. Posted {total_posted} suggestion(s), skipped {total_skipped}.")


if __name__ == "__main__":
    main()

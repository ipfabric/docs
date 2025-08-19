#!/usr/bin/env python3

import os
import re
import requests

from snakemd import Document

AUTH = None  # Assigned in main()
JIRA_BASE_URL = "https://ipfabric.atlassian.net/"
OUT_DIR = os.path.dirname(__file__) + "/docs/releases/release_notes_low-level/"
# Make sure, that project keys don't need any escaping!
# First project is used as a source of releases
PROJECT_KEYS = ("NIM", "DOS")


# Team name patterns to remove from ticket summaries (case-insensitive)
TEAM_CLEANUP_PATTERNS = [
    "[NAE]",
    "[FE]",
    "[BE]",
    "[OPS]",
]


def get_project_versions(project):
    response = requests.get(
        JIRA_BASE_URL + "rest/api/2/project/" + project + "/versions", auth=AUTH
    )
    response.raise_for_status()
    versions = response.json()
    versions = filter(
        lambda v: (v["archived"] is False and v["released"] is True), versions
    )

    return versions


def get_project_issues_from_version(project, projectVersion, startAt=0):
    additional_conditions = ""
    if project == "NIM":
        additional_conditions = " AND (resolution = Done) "
    jql = (
        "project = "
        + project
        + ' AND fixVersion = "'
        + projectVersion["name"]
        + '"'
        + additional_conditions
        + " AND (resolution IS NOT EMPTY OR statusCategory = Done) AND (labels NOT IN (skip_LLRN) OR labels IS EMPTY) ORDER BY key"
    )
    params = {
        "projectId": projectVersion["projectId"],
        "startAt": startAt,
        "maxResults": 1000,
        "jql": jql,
    }
    response = requests.get(
        JIRA_BASE_URL + "/rest/api/2/search", auth=AUTH, params=params
    )
    response.raise_for_status()
    return response.json()


def clean_title(summary):
    """Remove team name patterns from ticket summaries"""
    cleaned_summary = summary
    
    # Remove team names and trailing spaces
    for pattern in TEAM_CLEANUP_PATTERNS:
        cleaned_summary = re.sub(re.escape(pattern) + r'\s*', "", cleaned_summary, flags=re.IGNORECASE)
    
    # Clean up extra spaces and trim
    cleaned_summary = re.sub(r'\s+', ' ', cleaned_summary).strip()
    return cleaned_summary


def format_issue(issue):
    cleaned_summary = clean_title(issue['fields']['summary'])
    i = f"""
    `{issue['key']}` --
    {issue['fields']['priority']['name']} -- {cleaned_summary}
    """
    return i


def collect_issue_type_names(issues):
    names = []
    for issue in issues:
        name = issue["fields"]["issuetype"]["name"]
        if name not in names:
            names.append(name)
    names.sort()
    return names


def generate_release_notes(rn, project_issues):
    types = [
        (
            "Epic",
            "Epics",
            """Epics are high-level features, that may consist
            of many tasks.""",
        ),
        (
            "Story",
            "Stories",
            """Stories are high-level features, that may
            consist of many tasks. These would typically cover extensive
            functionality in IP Fabric""",
        ),
        (
            "Bug",
            "Bugs",
            """Anything that we considered an incorrect behavior.
            Something that was not working as expected or turned out that did
            not meet customers\' demand.""",
        ),
        (
            "Task",
            "Tasks",
            """Task may be associated
            into Epics or Stories to form complex features.""",
        ),
        (
            "Sub-task",
            "Sub-Tasks",
            """Sub-tasks are very well contained
            work packages, organized under Tasks.""",
        ),
    ]
    for type in types:
        issues = []
        for issue in project_issues:
            if issue["fields"]["issuetype"]["name"] == type[0]:
                issues.append(format_issue(issue))

        if len(issues) > 0:
            rn.add_heading(type[1], 3)
            rn.add_paragraph(type[2])
            rn.add_unordered_list(issues)

def main():
    global AUTH
    try:
        AUTH = (os.environ["JIRA_USER"], os.environ["JIRA_PASS"])
    except KeyError as err:
        print(f"Given key not found - {err}")
        print("You need to set JIRA_USER and JIRA_PASS environment variables")
        exit(1)

    branches = {}

    for v in get_project_versions(PROJECT_KEYS[0]):
        print(v)

        version_match = re.match(r"^(\d+)\.(\d+)\.(\d+)", v["name"])
        if not version_match:
            print(f"Unable to parse release name {v['name']}")
            continue

        major = int(version_match[1])
        minor = int(version_match[2])

#        if major < 7:
#            print(f"Skipping release {v['name']}")
#            continue

        # Include only versions 7.3 and later
        if (major * 1000 + minor) < 7003:
            print(f"Skipping release {v['name']}")
            continue

        branch_key = f"{major}.{minor}"
        if branch_key not in branches:
            branches[branch_key] = []
        branches[branch_key].append(v)

    for branch_key in sorted(branches.keys()):
        versions = sorted(branches[branch_key], key=lambda v: int(re.match(r"^(\d+)\.(\d+)\.(\d+)", v["name"]).group(3)), reverse=True)
        major, minor = branch_key.split(".")
        version_dir = f"{major}.x"
        file_name = f"{branch_key}.md"

        total_issues_in_branch = 0
        version_data = []

        for v in versions:
            print(f"Processing version {v['name']} in {branch_key}")

            issues = []
            issues_total = 0

            for project in PROJECT_KEYS:
                project_issues = []
                start_at = 0

                while True:
                    response = get_project_issues_from_version(project, v, start_at)
                    response_len = len(response["issues"])
                    print(
                        f"For {project} fetched {response_len}, so far {len(project_issues)}, should be {response['total']} issues"
                    )
                    project_issues += response["issues"]
                    start_at += response_len

                    if response_len == 0 or len(project_issues) == response["total"]:
                        break

                issues += project_issues
                issues_total += len(project_issues)
                total_issues_in_branch += len(project_issues)
                print(f"For {project} fetched {len(project_issues)} issues")

            if issues:
                version_data.append((v["name"], issues))

        rn = Document()
        rn.add_raw(
            f"---\n"
            f"description: IP Fabric automatically generated low-level release notes for version {branch_key}\n"
            f"search:\n"
            f"  boost: 0.5\n"
            f"---"
        )
        rn.add_heading(f"LLRN {branch_key}")
        rn.add_paragraph(
            f"These are low-level release notes for IP Fabric release branch `{branch_key}`. "
            "Please note, that this page contains very low-level information about the actual release, "
            "which can lead to false conclusions if you don’t have access to the tickets. "
            "On the other hand, it can provide valuable information, if you are looking for a particular detail. "
            f"This release branch contains a total of {total_issues_in_branch} fixed issues."
        )

        for version_name, issues in version_data:
            rn.add_heading(version_name, 2)
            generate_release_notes(rn, issues)

        os.makedirs(os.path.join(OUT_DIR, version_dir), exist_ok=True)
        with open(os.path.join(OUT_DIR, version_dir, file_name), "w") as file:
            print(rn, file=file)

if __name__ == "__main__":
    main()

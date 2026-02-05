#!/usr/bin/env python3

"""
Jira Support Team AI Agent
Creates release notes summaries from Jira tickets using PydanticAI
"""

import os
import re
import sys
from typing import Optional, List, Dict, Any
from dataclasses import dataclass
from enum import Enum

import requests
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from pydantic_ai import Agent


# Load environment variables
load_dotenv()

# Configuration
JIRA_BASE_URL = "https://ipfabric.atlassian.net/"
PROJECT_KEYS = ["NIM", "DOS", "IPF"]
JIRA_USER = os.getenv("JIRA_USER")
JIRA_PASS = os.getenv("JIRA_PASS")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not all([JIRA_USER, JIRA_PASS, OPENAI_API_KEY]):
    print("Error: Please set JIRA_USER, JIRA_PASS, and OPENAI_API_KEY in .env file")
    sys.exit(1)


class ReleaseType(Enum):
    """Type of release for different summarization approaches"""
    MAJOR_VERSION = "major"  # e.g., 7.5.0 - focus on new features and important fixes
    PATCH_VERSION = "patch"  # e.g., 7.5.21 - focus on fixes and improvements only


class ReleaseNotes(BaseModel):
    """Structured release notes output - only improvements and bug fixes for patch releases"""
    improvements: List[str] = Field(default_factory=list, description="Improvements and enhancements")
    bug_fixes: List[str] = Field(default_factory=list, description="Bug fixes")


@dataclass
class JiraContext:
    """Context for the AI agent with Jira data"""
    fix_version: str
    release_type: ReleaseType
    issues: List[Dict[str, Any]]
    total_issues: int


# ============================================================================
# JIRA API FUNCTIONS
# ============================================================================

def get_issues_by_fix_version(fix_version: str, project: str, next_page_token: Optional[str] = None) -> Dict[str, Any]:
    """
    Fetch issues for a specific fix version from Jira using the new API v3
    
    Args:
        fix_version: The fixVersion to filter by
        project: Project key (NIM, DOS, IPF)
        next_page_token: Token for pagination
        
    Returns:
        JSON response with issues and pagination info
    """
    additional_conditions = ""
    if project == "NIM":
        additional_conditions = " AND (resolution = Done) "
    
    jql = (
        f'project = {project} AND fixVersion = "{fix_version}"'
        f'{additional_conditions}'
        ' AND (resolution IS NOT EMPTY OR statusCategory = Done) '
        'AND (labels NOT IN (skip_LLRN) OR labels IS EMPTY) '
        'ORDER BY key'
    )
    
    params = {
        "jql": jql,
        "maxResults": 100,  # API limit for /search/jql
        "fields": "summary,issuetype,priority,description,labels,issuelinks,customfield_10014",  # Include epic link
    }
    
    if next_page_token:
        params["nextPageToken"] = next_page_token
    
    response = requests.get(
        JIRA_BASE_URL + "rest/api/3/search/jql",
        auth=(JIRA_USER, JIRA_PASS),
        params=params
    )
    response.raise_for_status()
    return response.json()


def fetch_all_issues(fix_version: str, projects: List[str]) -> List[Dict[str, Any]]:
    """
    Fetch all issues for a fix version across multiple projects
    
    Args:
        fix_version: The fixVersion to filter by
        projects: List of project keys
        
    Returns:
        List of all issues
    """
    all_issues = []
    
    for project in projects:
        print(f"Fetching issues for {project} in version {fix_version}...")
        next_page_token = None
        
        while True:
            response = get_issues_by_fix_version(fix_version, project, next_page_token)
            issues = response.get("issues", [])
            
            print(f"  Fetched {len(issues)} issues, total so far: {len(all_issues) + len(issues)}")
            all_issues.extend(issues)
            
            next_page_token = response.get("nextPageToken")
            if not next_page_token:
                break
    
    print(f"Total issues fetched: {len(all_issues)}")
    return all_issues


def determine_release_type(fix_version: str) -> ReleaseType:
    """
    Determine if this is a major version or patch based on version number
    
    Args:
        fix_version: Version string like "7.5.0" or "7.5.21"
        
    Returns:
        ReleaseType enum
    """
    match = re.match(r"^(\d+)\.(\d+)\.(\d+)", fix_version)
    if not match:
        return ReleaseType.PATCH_VERSION
    
    patch = int(match.group(3))
    
    # Versions ending in .0 or very low patch numbers (< 5) are considered major
    if patch <= 2:
        return ReleaseType.MAJOR_VERSION
    else:
        return ReleaseType.PATCH_VERSION


# ============================================================================
# HELPER FUNCTIONS FOR CATEGORIZATION
# ============================================================================

def extract_issue_info(issue: Dict[str, Any]) -> Dict[str, Any]:
    """Extract relevant information from a Jira issue"""
    fields = issue.get("fields", {})
    return {
        "key": issue.get("key"),
        "summary": fields.get("summary", ""),
        "description": fields.get("description", ""),
        "issuetype": fields.get("issuetype", {}).get("name", ""),
        "priority": fields.get("priority", {}).get("name", ""),
        "labels": fields.get("labels", []),
        "issuelinks": fields.get("issuelinks", []),
    }


def categorize_issues(issues: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Pre-categorize issues into improvements and bug fixes
    
    Returns:
        Dictionary mapping category names to lists of issues
    """
    categories = {
        "improvements": [],
        "bug_fixes": [],
    }
    
    for issue in issues:
        info = extract_issue_info(issue)
        issuetype = info["issuetype"]
        
        # Bug fixes - all bugs
        if issuetype == "Bug":
            categories["bug_fixes"].append(info)
        # Everything else goes to improvements
        else:
            categories["improvements"].append(info)
    
    return categories


# ============================================================================
# PYDANTIC AI AGENT
# ============================================================================

# Define the agent with OpenAI - using Pydantic model for structured output
agent = Agent(
    'openai:gpt-5.2-chat-latest',
    system_prompt="""You are a Jira Support Team AI Agent specialized in creating concise release notes.

Your task is to analyze Jira tickets and create very concise summaries (1 sentence per item) for release notes.

CRITICAL REQUIREMENT: For each ticket, you MUST check labels, summary, AND description for vendor/device family information and include it when found.

Guidelines:
1. This is for PATCH version release notes - focus on fixes and improvements only
2. Each item should be ONE sentence, but extract and include specific details FROM THE JIRA TICKETS:
   - ALWAYS check for and include device vendor/family when present (from labels or description)
   - Specific commands mentioned in the ticket
   - Specific error messages or issues described
   - Specific device models or vendors mentioned
   - Specific features, fields, columns, or components named
   - Specific API endpoints or database columns mentioned
   - Version numbers: ONLY include if it's a regression (mention when it was introduced)
   - DO NOT add generic consequences or benefits not in the ticket
   - DO NOT add information from external sources
3. Focus on WHAT WAS DONE based on ticket content, not WHY it was done
4. State facts from the tickets, not assumptions or generalizations
5. Be specific using details from ticket summaries and descriptions, not vague
6. Group changes intelligently by vendor/technology:
   - ONLY use vendor prefix (e.g., "Cisco ACI:") when there are 2+ fixes for that vendor
   - When grouping multiple fixes for the same vendor, use sub-bullets with a parent item
   - For single fixes, integrate the vendor name naturally into the description
   - DO NOT group unrelated vendors/technologies together
7. Use clear, professional language
8. Extract and include specific details ONLY from the ticket data:
   - FIRST check ticket labels for vendor (@vendor format, e.g., @cisco, @juniper, @arista, @fortinet, @paloalto)
   - SECOND check ticket labels for device families (@family format, e.g., @nxos = NX-OS, @eos = EOS, @iosxe = IOS-XE, @fortigate = FortiGate)
   - THIRD check ticket labels for technologies (!technology format, e.g., !aci = ACI, !bgp = BGP, !vlan = VLAN)
   - FOURTH thoroughly scan ticket summary for vendor/device mentions (Cisco, Juniper, Arista, Fortinet, Palo Alto, etc.)
   - FIFTH thoroughly scan ticket description for vendor/device/family mentions (NX-OS, IOS-XE, EOS, FortiGate, etc.)
   - ALWAYS include vendor/family in the release note if found in ANY of these places
   - Extract exact command names, error messages, or field names from the ticket
   - Extract exact feature names, table names, or column names mentioned
   - Version numbers: ONLY include if ticket explicitly mentions this is a regression and states which version introduced the issue
   - Avoid adding context or implications not present in the ticket
9. For vendor support improvements, extract from ticket:
   - Vendor from labels (@vendor) or description
   - Device family from labels (@family) or description
   - Technologies from labels (!technology) or description
   - Specific commands mentioned in the ticket
   - Specific protocols or features named in the ticket

Style Examples:

Single vendor fix (ONLY 1 item for this vendor - NO PREFIX):
✅ CORRECT: "Fixed empty MAC address table issue on Juniper devices"
✅ CORRECT: "Corrected firewall policy evaluation on Fortinet FortiGate devices when explicit allow policy is present"
✅ CORRECT: "Fixed BGP neighbor state tracking on Cisco IOS-XE devices"
✅ CORRECT: "Corrected VLAN interface handling on Arista EOS switches"
✅ CORRECT: "Fixed missing 'siteName' column in device inventory tables" (no vendor = platform fix)

❌ WRONG - NEVER DO THIS FOR SINGLE ITEMS:
❌ "Fortinet FortiGate fix: Corrected firewall..."
❌ "Fortinet FortiGate: Corrected firewall..."
❌ "Juniper devices: Fixed empty MAC table"
❌ "Cisco NX-OS: Fixed BGP neighbor state"
❌ "Cisco IOS-XE fix: Corrected VLAN handling"

If you see ONLY ONE item for a vendor, integrate vendor naturally in the sentence!

Multiple fixes for same vendor/family (2+ items - USE PARENT with sub-bullets):

✅ CORRECT - Group all Cisco NX-OS items together:
"Cisco NX-OS fixes:
  - Fixed MAC address table parsing
  - Corrected VLAN interface handling
  - Resolved BGP neighbor state tracking
  - Fixed interface speed detection
  - Corrected routing table parsing"
  
✅ CORRECT - Group all Cisco ACI items together:
"Cisco ACI fixes:
  - Fixed failures in loading graphs
  - Corrected switching instead of routing mode  
  - Resolved Path Lookup failure caused by 'Traffic loop detected' error"
  
✅ CORRECT - Group items even if wording varies (NX-OS, Nexus, Cisco Nexus):
"Cisco NX-OS fixes:
  - Fixed MAC parsing on Nexus devices
  - Corrected VLAN handling in NX-OS
  - Resolved issue on Cisco Nexus 9000"
  
❌ WRONG - Separate bullets when they should be grouped:
"- Fixed MAC table parsing on Cisco NX-OS devices"
"- Corrected VLAN interface on Cisco Nexus switches"
"- Resolved BGP on NX-OS routers"
(All should be grouped under ONE "Cisco NX-OS fixes:" parent)

❌ WRONG - Using prefix on individual items:
"- Cisco ACI: Fixed graphs"
"- Cisco ACI: Corrected mode"
(Should be ONE parent "Cisco ACI fixes:" with sub-bullets)

Other examples (extract details from ticket, don't add consequences):
✅ GOOD: "Updated 'expect' script to avoid logging passwords" (exact script name from ticket)
✅ GOOD: "Enabled copy and paste functionality from Excel into IP address list filters" (exact feature from ticket)
✅ GOOD: "Fixed missing 'IsUnlicensed' column in version 7.3 PostgreSQL database" (exact column name and version from ticket)
✅ GOOD: "Resolved error 'column dev.attributes does not exist' in GCP Inventory table" (exact error message from ticket)
✅ GOOD: "Corrected passing traffic values in Path Lookup" (if ticket mentions 'passing traffic values')
❌ BAD: "Fixed memory leak to improve performance" (adding 'improve performance' not in ticket)
❌ BAD: "Updated script for better security" (adding 'better security' not in ticket)
❌ BAD: "Improved API" (too vague, not using ticket specifics)
❌ BAD: "Fixed issue in database" (not using exact error or table name from ticket)

Only add reasons/benefits when:
- The change is complex and needs context
- The impact is significant and not obvious from the description

Categories to populate (ONLY TWO):
- Improvements: All enhancements including vendor support, GUI changes, path lookup improvements, network discovery, experimental features
- Bug Fixes: ALL bug fixes and corrections, including:
  - Data collection/parsing fixes
  - Algorithm fixes
  - UI/display fixes
  - Performance fixes
  - API fixes
  - Any issue resolution or correction
  
Note: If a fix affects many customers or specific vendors, mention that for context.

Only include categories that have relevant content. Skip empty categories.

You must respond with a JSON object matching the ReleaseNotes schema.""",
)


async def generate_release_notes(context: JiraContext) -> ReleaseNotes:
    """
    Generate release notes using the AI agent
    
    Args:
        context: JiraContext with version info and issues
        
    Returns:
        Structured ReleaseNotes object
    """
    # Categorize issues first
    categorized = categorize_issues(context.issues)
    
    # Build a prompt with the categorized issues
    prompt_parts = [
        f"Create release notes for version {context.fix_version}.",
        f"Release type: {context.release_type.value}",
        f"Total issues: {context.total_issues}",
        "",
    ]
    
    if context.release_type == ReleaseType.MAJOR_VERSION:
        prompt_parts.append("This is a MAJOR version - focus on new features and important improvements.")
    else:
        prompt_parts.append("This is a PATCH version - focus on fixes and improvements only.")
    
    prompt_parts.append("")
    prompt_parts.append("Categorized issues:")
    
    prompt_parts.append("\n" + "="*80)
    prompt_parts.append("CRITICAL: For EACH ticket below, check ALL of these for vendor/family:")
    prompt_parts.append("  1. Labels with @vendor (e.g., @cisco, @juniper, @arista, @fortinet)")
    prompt_parts.append("  2. Labels with @family (e.g., @nxos=NX-OS, @iosxe=IOS-XE, @eos=EOS, @fortigate=FortiGate)")
    prompt_parts.append("  3. Labels with !technology (e.g., !aci=ACI, !bgp=BGP, !vlan=VLAN)")
    prompt_parts.append("  4. Ticket SUMMARY - scan for vendor names (Cisco, Juniper, Arista, Fortinet, etc.)")
    prompt_parts.append("  5. Ticket DESCRIPTION - scan for vendor/family names (NX-OS, IOS-XE, EOS, FortiGate, etc.)")
    prompt_parts.append("INCLUDE vendor/family in release note if found in ANY of these places!")
    prompt_parts.append("="*80 + "\n")
    
    for category, issues_list in categorized.items():
        if issues_list:
            prompt_parts.append(f"\n{category.upper()} ({len(issues_list)} issues):")
            for issue in issues_list[:100]:  # Limit to first 20 per category for context
                prompt_parts.append(f"  - [{issue['key']}] {issue['summary']}")
                if issue['labels']:
                    # Highlight vendor, family, and technology labels
                    labels_str = ", ".join(issue['labels'])
                    prompt_parts.append(f"    Labels: {labels_str}")
                if issue['description']:
                    desc_snippet = str(issue['description'])[:800]
                    prompt_parts.append(f"    Description: {desc_snippet}...")
    
    # For patch versions, analyze all categories but merge into only improvements and bug fixes
    prompt_parts.append("\n\nReturn a JSON object with ONLY these sections:")
    prompt_parts.append("""{
  "improvements": ["item1", "item2"],
  "bug_fixes": ["item1", "item2"]
}

IMPORTANT GROUPING RULES - FOLLOW THIS PROCESS:

STEP 1: First, create individual release notes for each ticket with vendor/family included naturally.

STEP 2: Then, analyze ALL release notes and look for patterns:
- Find ALL items mentioning the SAME vendor/family (e.g., "Cisco NX-OS", "Cisco Nexus", "Fortinet FortiGate", "Arista EOS")
- Count how many items there are for each vendor/family
- If 2+ items exist for the SAME vendor/family, GROUP THEM

STEP 3: Apply grouping:
- 2+ items for same vendor/family → Create parent with sub-bullets:
  "Cisco NX-OS fixes:\\n  - Fixed MAC table parsing\\n  - Corrected VLAN handling\\n  - Resolved BGP state"
- Only 1 item for a vendor/family → Keep as single sentence (NO PREFIX):
  "Fixed empty MAC table on Juniper devices" (NOT "Juniper: Fixed empty MAC table")

STEP 4: Normalize vendor/family names:
- "Cisco NX-OS", "Cisco Nexus", "NX-OS" → All group as "Cisco NX-OS"
- "Cisco ACI", "ACI" → All group as "Cisco ACI"
- "Fortinet FortiGate", "FortiGate" → All group as "Fortinet FortiGate"
- "Arista EOS", "EOS", "Arista" → All group as "Arista EOS"

CRITICAL: NEVER use prefix (like "Vendor:") for single items!

CRITICAL: Vendor/family identification AND grouping process:
1. For EACH ticket, identify vendor/family by checking:
   - Labels: @vendor, @family, !technology
   - Summary: vendor names (cisco, juniper, arista, fortinet, palo alto, etc.)
   - Description: vendor/family names (NX-OS, IOS-XE, EOS, FortiGate, Junos, ASA, etc.)

2. Group tickets with SAME vendor/family combination:
   - Multiple Cisco ACI tickets → "Cisco ACI fixes:" with sub-bullets
   - Multiple Cisco NX-OS tickets → "Cisco NX-OS fixes:" with sub-bullets
   - Multiple Fortinet FortiGate tickets → "Fortinet FortiGate fixes:" with sub-bullets
   - Single ticket → integrate vendor naturally in sentence (NO prefix)

3. Common vendor/family patterns:
   - Cisco (NX-OS, IOS-XE, IOS, ASA, ACI)
   - Juniper (Junos, MX, EX, SRX)
   - Arista (EOS)
   - Fortinet (FortiGate, FortiOS)
   - Palo Alto (PAN-OS)
   - HP/HPE (Aruba, Comware, ProCurve)

4. If no vendor after checking all sources, acceptable for platform fixes

This is a PATCH release, so organize ALL tickets into only these two categories:
- "improvements": Include ALL enhancements, vendor support improvements, GUI changes, path lookup improvements, network discovery improvements, and experimental features
- "bug_fixes": Include ALL bug fixes, corrections, and issue resolutions (parsing fixes, algorithm fixes, UI fixes, performance fixes, API fixes, etc.)

CRITICAL PROCESS TO FOLLOW:
1. First pass: Create individual release notes for each ticket (with vendor/family naturally integrated)
2. Second pass: Analyze ALL release notes and identify patterns
3. Group items: Find all items with same vendor/family and group them (2+ items = parent with sub-bullets)
4. Final check: Ensure NO single items have vendor prefix (e.g., "Vendor:", "Vendor fix:")

Examples of vendor/family variations to group together:
- "Cisco NX-OS", "Cisco Nexus", "NX-OS" → Group as "Cisco NX-OS fixes:"
- "Cisco ACI", "ACI" → Group as "Cisco ACI fixes:"
- "Fortinet FortiGate", "FortiGate" → Group as "Fortinet FortiGate fixes:"

Only include categories with content. Create concise, user-focused summaries.""")
    
    prompt = "\n".join(str(p) for p in prompt_parts)
    
    result = await agent.run(prompt, message_history=[])
    
    # Parse the response as ReleaseNotes
    # In PydanticAI, the result content is in different attributes depending on version
    response_text = None
    
    # Try different attribute names
    for attr in ['data', 'output', 'content', 'result', 'response', 'text']:
        if hasattr(result, attr):
            response_text = getattr(result, attr)
            break
    
    if response_text is None:
        # Try to get the string representation
        response_text = str(result)
    
    if isinstance(response_text, str):
        import json
        # Try to extract JSON from the response
        try:
            # First, try to extract from code blocks (```json ... ```)
            code_block_match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', response_text, re.DOTALL)
            if code_block_match:
                json_str = code_block_match.group(1)
                data = json.loads(json_str)
                return ReleaseNotes(**data)
            
            # Look for JSON object (more aggressive pattern)
            # Find the outermost complete JSON object
            brace_count = 0
            start_idx = response_text.find('{')
            if start_idx != -1:
                for i, char in enumerate(response_text[start_idx:], start=start_idx):
                    if char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            json_str = response_text[start_idx:i+1]
                            data = json.loads(json_str)
                            return ReleaseNotes(**data)
            
        except Exception as e:
            print(f"Warning: Could not parse JSON response: {e}")
        # If parsing fails, return empty notes
        return ReleaseNotes()
    elif isinstance(response_text, dict):
        # If it's already a dict, try to create ReleaseNotes from it
        try:
            return ReleaseNotes(**response_text)
        except Exception as e:
            print(f"Warning: Could not create ReleaseNotes from dict: {e}")
            return ReleaseNotes()
    
    return response_text if isinstance(response_text, ReleaseNotes) else ReleaseNotes()


# ============================================================================
# INTERACTIVE CONVERSATION
# ============================================================================

async def interactive_refinement(release_notes: ReleaseNotes, context: JiraContext) -> ReleaseNotes:
    """
    Allow user to interact with the agent to refine release notes
    
    Args:
        release_notes: Initial release notes
        context: JiraContext for additional queries
    """
    # Prepare the full ticket data for the agent to reference
    categorized = categorize_issues(context.issues)
    
    # Build a comprehensive context with all ticket details
    ticket_context = [
        f"=== ORIGINAL TICKET DATA FOR VERSION {context.fix_version} ===",
        f"Total tickets: {context.total_issues}",
        f"Release type: {context.release_type.value}",
        ""
    ]
    
    for category, issues_list in categorized.items():
        if issues_list:
            ticket_context.append(f"\n{category.upper()} ({len(issues_list)} tickets):")
            for issue in issues_list:
                ticket_context.append(f"\n[{issue['key']}] {issue['summary']}")
                ticket_context.append(f"  Type: {issue['issuetype']}")
                ticket_context.append(f"  Priority: {issue['priority']}")
                if issue['description']:
                    desc = str(issue['description'])[:800]
                    ticket_context.append(f"  Description: {desc}")
                if issue['labels']:
                    ticket_context.append(f"  Labels: {', '.join(issue['labels'])}")
    
    full_ticket_context = "\n".join(ticket_context)
    
    conversation_agent = Agent(
        'openai:gpt-4o',
        system_prompt=f"""You are helping refine release notes with access to all original ticket data.

The user may ask you to:
- Add more details to specific sections
- Rephrase items for clarity
- Add or remove items
- Change the tone or focus
- Ask questions about specific tickets
- Reference specific ticket details from the original data

You have access to ALL original ticket information including summaries, descriptions, types, priorities, and labels.
Use this data to provide accurate and detailed responses when refining the release notes.

Always maintain the concise, professional style of release notes (1-2 sentences per item).

IMPORTANT: When the user asks to make changes to the release notes, you MUST:
1. First, briefly explain what changes you're making
2. Then provide the COMPLETE updated release notes in JSON format wrapped in ```json ``` code blocks

The JSON format should be:
```json
{{
  "improvements": ["item1", "item2"],
  "bug_fixes": ["item1", "item2"]
}}
```

Only include sections that have content. Include ALL items, not just the changed ones.

{full_ticket_context}"""
    )
    
    print("\n" + "="*80)
    print("Interactive Mode - You can now refine the release notes")
    print("="*80)
    print("\nCommands:")
    print("  - Ask for changes: 'Add more details about API changes'")
    print("  - Ask questions: 'What does ticket NIM-1234 do?'")
    print("  - Request specific refinements: 'Make the bug fixes more specific'")
    print("  - Type 'done' to finish")
    print("  - Type 'show' to display current release notes")
    print()
    
    current_notes = release_notes
    conversation_history = [
        f"Current release notes for version {context.fix_version}:\n{format_release_notes(current_notes)}"
    ]
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if not user_input:
            continue
        
        if user_input.lower() in ['done', 'exit', 'quit']:
            print("\nFinishing up...")
            break
        
        if user_input.lower() == 'show':
            print("\n" + "="*80)
            print("CURRENT RELEASE NOTES")
            print("="*80)
            print(format_release_notes(current_notes))
            continue
        
        # Add user message to history
        conversation_history.append(f"User: {user_input}")
        
        # Get AI response
        prompt = "\n\n".join(conversation_history)
        result = await conversation_agent.run(prompt)
        
        # Get response text from result
        if hasattr(result, 'data'):
            response = result.data
        elif hasattr(result, 'output'):
            response = result.output
        elif hasattr(result, 'content'):
            response = result.content
        else:
            response = str(result)
        
        conversation_history.append(f"Assistant: {response}")
        print(f"\nAssistant: {response}")
        
        # Check if the response contains updated release notes in JSON format
        if '{' in response and any(key in response for key in ['improvements', 'bug_fixes', 'new_features']):
            try:
                import json
                
                # First try to extract from code blocks
                code_block_match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', response, re.DOTALL)
                if code_block_match:
                    json_str = code_block_match.group(1)
                else:
                    # Try to find JSON object with brace matching
                    brace_count = 0
                    start_idx = response.find('{')
                    if start_idx != -1:
                        for i, char in enumerate(response[start_idx:], start=start_idx):
                            if char == '{':
                                brace_count += 1
                            elif char == '}':
                                brace_count -= 1
                                if brace_count == 0:
                                    json_str = response[start_idx:i+1]
                                    break
                        else:
                            json_str = None
                    else:
                        json_str = None
                
                if json_str:
                    data = json.loads(json_str)
                    current_notes = ReleaseNotes(**data)
                    print("\n✅ Release notes updated successfully!")
                    conversation_history[-1] = f"Assistant: {response}\n\nUpdated release notes:\n{format_release_notes(current_notes)}"
            except Exception as e:
                print(f"\n⚠️  Note: Could not parse updated release notes: {e}")
                pass  # If parsing fails, just keep the text response
    
    return current_notes


def format_release_notes(notes: ReleaseNotes) -> str:
    """Format release notes as readable text"""
    sections = []
    
    if notes.improvements:
        sections.append("### Improvements\n" + "\n".join(f"- {item}" for item in notes.improvements))
    
    if notes.bug_fixes:
        sections.append("### Bug Fixes\n" + "\n".join(f"- {item}" for item in notes.bug_fixes))
    
    return "\n\n".join(sections)


# ============================================================================
# MAIN
# ============================================================================

async def main():
    """Main entry point"""
    print("="*80)
    print("Jira Support Team AI Agent - Patch Release Notes Generator")
    print("="*80)
    print("\nThis tool is designed for PATCH version release notes.")
    print("It generates 'Improvements' and 'Bug Fixes' sections only.")
    print()
    
    # Get fix version from user
    fix_version = input("Enter fixVersion (e.g., 7.5.0 or 7.5.21): ").strip()
    
    if not fix_version:
        print("Error: fixVersion is required")
        sys.exit(1)
    
    # Determine release type
    release_type = determine_release_type(fix_version)
    print(f"\nDetected release type: {release_type.value}")
    
    # Warn if it's a major version
    if release_type == ReleaseType.MAJOR_VERSION:
        print("\n⚠️  WARNING: This appears to be a major version release.")
        print("This script is optimized for patch releases and will only generate 'Improvements' and 'Bug Fixes' sections.")
        print("For major version releases with full categorization, consider manual release notes creation.")
        proceed = input("\nContinue anyway? (y/n): ").strip().lower()
        if proceed != 'y':
            print("Exiting...")
            sys.exit(0)
    
    # Fetch all issues
    print("\nFetching issues from Jira...")
    issues = fetch_all_issues(fix_version, PROJECT_KEYS)
    
    if not issues:
        print(f"\nNo issues found for version {fix_version}")
        sys.exit(1)
    
    # Create context
    context = JiraContext(
        fix_version=fix_version,
        release_type=release_type,
        issues=issues,
        total_issues=len(issues)
    )
    
    # Generate release notes
    print("\nGenerating release notes with AI...")
    release_notes = await generate_release_notes(context)
    
    # Display initial release notes
    print("\n" + "="*80)
    print(f"RELEASE NOTES FOR VERSION {fix_version}")
    print("="*80)
    print(format_release_notes(release_notes))
    
    # Interactive refinement
    proceed = input("\nWould you like to refine the release notes? (y/n): ").strip().lower()
    if proceed == 'y':
        release_notes = await interactive_refinement(release_notes, context)
        print("\n" + "="*80)
        print("FINAL RELEASE NOTES")
        print("="*80)
        print(format_release_notes(release_notes))
    
    # Save to file
    output_file = f"release_notes_{fix_version.replace('.', '_')}.md"
    with open(output_file, 'w') as f:
        f.write(f"# Release Notes - Version {fix_version}\n\n")
        f.write(format_release_notes(release_notes))
    
    print(f"\nRelease notes saved to: {output_file}")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

#!/usr/bin/env python3

import os
import re
import requests

from snakemd import Document

AUTH = None  # Assigned in main()
JIRA_BASE_URL = 'https://ipfabric.atlassian.net/'
OUT_DIR = os.path.dirname(__file__)+'/docs/releases/release_notes_low-level/'
# Make sure, that project keys don't need any escaping!
# Firs project is used as a source of releases
PROJECT_KEYS = ('NIM', 'DOS')


def get_project_versions(project):
    response = requests.get(JIRA_BASE_URL + 'rest/api/2/project/' + project +
                            '/versions', auth=AUTH)
    response.raise_for_status()
    versions = response.json()
    versions = filter(lambda v: (v['archived'] is False
                                 and v['released'] is True), versions)

    return versions


def get_project_issues_from_version(project, projectVersion, startAt=0):
    additional_conditions = ''
    if project == "NIM":
        additional_conditions = ' AND (resolution = Done) '
    jql = ('project = ' + project + ' AND fixVersion = "'
           + projectVersion['name'] + '"' + additional_conditions +
           ' AND (resolution IS NOT EMPTY OR statusCategory = Done) AND (labels NOT IN (skip_LLRN) OR labels IS EMPTY) ORDER BY key')
    params = {
                'projectId': projectVersion['projectId'],
                'startAt': startAt,
                'maxResults': 1000,
                'jql': jql,
            }
    response = requests.get(
            JIRA_BASE_URL + '/rest/api/2/search', auth=AUTH, params=params)
    response.raise_for_status()
    return response.json()


def format_issue(issue):
    i = f"""
    `{issue['key']}` --
    {issue['fields']['priority']['name']} -- {issue['fields']['summary']}
    """
    return(i)


def collect_issue_type_names(issues):
    names = []
    for issue in issues:
        name = issue['fields']['issuetype']['name']
        if name not in names:
            names.append(name)
    names.sort()
    return names


def generate_release_notes(rn, project_issues):
    types = [
        ('Epic', 'Epics', '''Epics are high-level features, that may consist
            of many tasks.'''),
        ('Story', 'Stories', '''Stories are high-level features, that may
            consist of many tasks. These would typically cover extensive
            functionality in IP Fabric'''),
        ('Bug', 'Bugs', '''Anything that we considered an incorrect behavior.
            Something that was not working as expected or turned out that did
            not meet customers\' demand.'''),
        ('Task', 'Tasks', '''Task may be associated
            into Epics or Stories to form complex features.'''),
        ('Sub-task', 'Sub-Tasks', '''Sub-tasks are very well contained
            work packages, organized under Tasks.''')
    ]
    for type in types:
        issues = []
        for issue in project_issues:
            if issue['fields']['issuetype']['name'] == type[0]:
                issues.append(format_issue(issue))

        if len(issues) > 0:
            rn.add_header(type[1], 2)
            rn.add_paragraph(type[2])
            rn.add_unordered_list(issues)


def main():
    global AUTH
    try:
        AUTH = (os.environ['JIRA_USER'], os.environ['JIRA_PASS'])
    except KeyError as err:
        print(f"Given key not found - {err}")
        print("You need to set JIRA_USER and JIRA_PASS environment variables")
        exit(1)

    for v in get_project_versions(PROJECT_KEYS[0]):
        print(v)

        version_match = re.match(r'^(\d+)\.(\d+)\.(\d+)', v['name'])
        if not version_match:
            print(f"Unable to parse release name {v['name']}")
            continue

        major = int(version_match[1])
        minor = int(version_match[2])

        # Include only versions 5.0 and later
        if (major*1000 + minor) < 5000:
            print(f"Skipping release {v['name']}")
            continue

        version_dir = f"{major}.x/{major}.{minor}.x"

        issues = []
        issues_total = 0

        for project in PROJECT_KEYS:
            project_issues = []
            start_at = 0

            while True:
                response = get_project_issues_from_version(project, v, start_at)
                response_len = len(response['issues'])
                print(f"For {project} fetched {response_len}, so far {len(project_issues)}, should be {response['total']} issues")
                # print(json.dumps(response['issues'], indent=2))

                project_issues += response['issues']
                start_at += response_len

                if (response_len == 0 or len(project_issues) == response['total']):
                    # We have fetched all results or we got empty response
                    # maybe because we have iterated beyond the end of the list
                    break


            issues += project_issues
            issues_total += len(project_issues)
            print(f"For {project} fetched {len(project_issues)} issues")

        rn = Document("release_notes")
        rn.add_header(f"LLRN {v['name']}")
        rn.add_paragraph(f""" These are low-level release notes for IP Fabric
                release `{v['name']}`. Please note, that this page contains
                very low-level information about the actual release, which can
                lead to false conclusions if you don't have access to the
                tickets. On the other hand, it can provide valuable information,
                if you are looking for a particular detail. This release of
                IP Fabric contains a total of {issues_total} issues.""")

        generate_release_notes(rn, issues)

        os.makedirs(os.path.join(OUT_DIR, version_dir), exist_ok=True)
        with open(os.path.join(
                OUT_DIR, version_dir, v['name'] + '.md'), 'w') as file:
            print(rn, file=file)


if __name__ == '__main__':
    main()

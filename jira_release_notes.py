#!/usr/bin/env python3

import os
import re
import requests

from snakemd import Document

AUTH = None  # Assigned in main()
JIRA_BASE_URL = 'https://ipfabric.atlassian.net/'
OUT_DIR = 'docs/releases/low-level_release_notes/'
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


def get_project_issues_from_version(project, projectVersion):
    jql = ('project = ' + project + ' AND fixVersion = "'
           + projectVersion['name'] +
           '" AND (resolution IS NOT EMPTY OR statusCategory = Done) ORDER BY key')
    params = {
                'projectId': projectVersion['projectId'],
                'maxResults': 1000,
                'jql': jql,
            }
    response = requests.get(
            JIRA_BASE_URL + '/rest/api/2/search', auth=AUTH, params=params)
    response.raise_for_status()
    return response.json()


def issue_browse_url(issue):
    return(JIRA_BASE_URL + 'browse/' + issue['key'])


def format_issue(issue):
    i = f"""
    [{issue['key']}]({issue_browse_url(issue)}) --
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
        ('Epic', 'Epics', '''Epics are high-level features, which may consist
            of many tasks.'''),
        ('Story', 'Stories', '''Stories are high-level features, which may
            consist of many tasks. These would typically cover large
            functionality in IP Fabric'''),
        ('Bug', 'Bugs', '''Anything what we considered an incorrect behavior.
            Something what was not working as intended or turned out that does
            not meet customers demand.'''),
        ('Task', 'Tasks', '''A typical unit of work. They may be associated
            into Epics or Stories to form large features.''')
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
        if not re.match(r'^[456789]\.\d+\.\d+', v['name']):
            print(f"Skipping release {v['name']}")
            continue

        version_dir = re.match(r'^(\d+\.\d+).\d+', v['name'])[1] + '.x'

        issues = []
        issues_total = 0

        for project in PROJECT_KEYS:
            project_issues = get_project_issues_from_version(project, v)
            print(f"For {project} fetched {project_issues['total']} issues")
            # print(json.dumps(projectIssues, indent=2))
            issues += project_issues['issues']
            issues_total += project_issues['total']

        rn = Document("release_notes")
        rn.add_header(f"LLRN {v['name']}")
        rn.add_paragraph(f""" These are low-level release notes for IP Fabric
                release `{v['name']}`. Please note, that this page contains
                very low-level information about the actual release, which can
                lead to false conclusions if you don't have access to the
                tickets. On the other hand we believe, that it can provide a
                valuable information, if you are looking for particular detail.
                This release of IP Fabric contains total of
                {issues_total} issues. And was internally released
                on {v['releaseDate']}. """)

        generate_release_notes(rn, issues)

        os.makedirs(os.path.join(OUT_DIR, version_dir), exist_ok=True)
        with open(os.path.join(
                OUT_DIR, version_dir, v['name'] + '.md'), 'w') as file:
            print(rn, file=file)


if __name__ == '__main__':
    main()
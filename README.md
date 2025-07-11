# IP Fabric Documentation Project

We are using [MkDocs](https://www.mkdocs.org/) with the excellent [Material for
MkDocs](https://squidfunk.github.io/mkdocs-material/). Last but not least, there
is [mike](https://github.com/jimporter/mike), which is a tool for building and
publishing different versions of the documentation.

## Release Process

One of the main motivations for migrating towards Markdown-based documentation
is the ability to follow a standard development model. Thus, any update to the
documentation happens as follows:

- Create your "feature" branch. It is good practice to include a ticket number
  at the beginning. For example, `NIM-5808_readme`.
- Do all your commits in the branch. When ready, open a merge request (MR) on
  GitLab (also make sure that it starts with your ticket number, correctly
  formatted).
- Set yourself as the assignee (as you are the owner of the MR).
- At the moment, please set the reviewer to @antonin.kral-ipf and/or
  @zdenek.sindylek-ipf for all your MRs.
- The CI/CD pipeline builds and publishes on every push to `main`.
- `mike` is then used by repository maintainers to push a new version release to
  the documentation web. (See the `mike` section below.)

## Writing Documentation

### Style Guide

- Make sure you use relative links, otherwise you'd break versioned links.
- Make sure your links work -- esp. please make sure your internal links are
  relative (usually this means they're starting with `..`, internal links must
  not start with `/` or even `https://` as these would not work correctly when
  deployed).
- Build a list of unordered items by using hyphens (`-`), instead of `*`.
- If you use an abbreviation, make sure you define it first.
  - Abbreviations are always uppercase, unless used in a verbatim text (e.g.
    in an API call) when they need to be marked as `monotype`.
- Verbatim strings are to be rendered in `monotype` (backticks) -- e.g. API call
  parameters, command-line arguments etc.
- Please use regular double quotes -- the `"` character instead of fancy/curly
  UTF-8 quotes.
- Consider using [snippets](snippets) for content repeated / copy-pasted through
  multiple pages.

Look at e.g.:

- <https://github.com/errata-ai/vale-boilerplate/tree/master/styles/Microsoft>
- <https://grafana.com/docs/writers-toolkit/writing-guide/markdown-guide/>

### CI/CD

We are using [Vale](https://github.com/errata-ai/vale) to help you keep a
consistent documentation style. It keeps an eye on your choice of words, tenses,
sentence complexity, and much more. It is run as a part of the CI/CD pipeline.

A failure is not a fatal error at the moment, but please look into CI/CD logs
during MR to avoid adding new problems.

We also build the documentation during CI/CD which means that internal links
are being validated.

### General Recommendations

There are some great resources on how to write a good documentation out on
Interwebs. Good starting points:

- [Google's Technical Documentation Style Guide](https://developers.google.com/style)
- [Google's Technical Writing Course](https://developers.google.com/tech-writing)

### Repository Layout

All the documents live under the `docs` directory. Directories are used to
create sections. Please pay attention to naming. We have opted for automated
content discovery which honors alphabetical order.

- Directory names are translated directly to chapter names. Please use English
  capitalization rules for directory/file names.
- Words in directory/file names are separated by underscores `_`.

Another approach would be manual configuration with `nav` section, but that
would require manual addition of every single new page. This approach is
similar in other documentation builders (except Sphinx). You can read more at
[MkDocs documentation on file
layout](https://www.mkdocs.org/user-guide/writing-your-docs/).

Instead, we have opted for `awesome-pages` plugin, which allows for a
combination of manual navigation entries as well as automated ones (based on
filenames). Check the `.pages.yml` file in the directories.

### Including Documentation From Other Repositories

You can include content from other repositories. This is especially useful
for integrations. We have opted for [`mkdocs-multirepo-plugin`](https://github.com/jdoiro3/mkdocs-multirepo-plugin).

A basic configuration looks like:

```yaml
plugins:
  - multirepo:
      cleanup: false
      temp_dir: temp_multirepo
      repos:
        - section: 'pokus'
          section_path: 'integrations'
          import_url: 'https://gitea.bobek.cc/bobek/pokus_docs.git?branch=main'
        - section: 'monorepo'
          section_path: 'integrations'
          import_url: 'git@gitlab.com:ip-fabric/development/product/ipfabric-product.git?branch=main&docs_dir=doc/*'
```

This will bring two repositories under `integrations/` path and name them as
`pokus` and `monorepo`. The first one is a public repository, the second one is
a private one. For private, you need to add `docs_ci_bot` deploy key to your
repository (read-only access).

It also demonstrates the use of `docs_dir` to pick a custom directory from
within the repository.

`temp_multirepo` is a temporary directory used for cloning repositories. It
contains pulled pages in a correct structure. It's also used for linters.

### Writing Your Documents

Documents are written in [Markdown](https://www.markdownguide.org/cheat-sheet/)
with some helpful extensions. List of enabled extensions is in `mkdocs.yml`
under the `markdown_extensions` section.

- [admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)
  for callouts like "example", "note", "warning" etc.
- [attr_list](https://squidfunk.github.io/mkdocs-material/reference/buttons/)
  for nice buttons
- [def_list](https://squidfunk.github.io/mkdocs-material/reference/lists/#using-definition-lists)
  for definition lists

Please make yourself familiar with
[Material Reference Guide](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/)
and
[MkDocs Markdown Guide](https://www.mkdocs.org/user-guide/writing-your-docs/#writing-with-markdown).

### GitHub Mirror and Public Sources

Our documentation is open to public at <https://docs.ipfabric.io> . We went one
step further and also made the source code for the documentation open at
<https://github.com/ipfabric/docs> . This allows customers to not only closely
follow updates, but also to provide improvements. Every page also has an
**Edit this page** button to simplify this process.

#### Handling Contribution (Pull Request on GitHub)

The primary source of data is GitLab, where also the majority of reviews takes
place. GitLab pushes updates to GitHub (it automatically mirrors all protected
branches). This means that the final merge needs to happen on the GitLab side.
The rough process for handling contribution is as follows:

- A contributor creates a pull request (PR) on GitHub.
- People with access to GitHub do the review with the contributor using GitHub's
  PR interface.
- The remote branch is pulled from GitHub and pushed to GitLab, where a new
  merge request (MR) is created. CI runs at this time for the MR on the GitLab
  side.
- When merged to `main` (or other appropriate branch) on the GitLab side, code
  is pushed to GitHub. A responsible person needs to go to GitHub and close the
  opened pull request manually.

### Live Preview

#### Container

You can run a live preview, which is super helpful when writing / editing the
documentation. If you are an IP Fabric insider, it is as simple as (check the
[GitLab container registry](https://docs.gitlab.com/ee/user/packages/container_registry/#authenticate-with-the-container-registry)
documentation, if you don't have it authenticated):

```shell
make serve
```

Please note that it will utilize `--dirtyreload` which can lead to
inconsistencies, but is significantly faster to reload, when editing just a
couple of pages.

#### Python Virtual Environment

If you don't have access to the internal container image, you can alternatively utilize a Python virtual environment.

**Prerequisites** 

The `cairo` library must be installed and available in the PATH.

* _Mac OS users_ -- Install the library via `brew install cairo`.
* _Windows users_ -- Follow [GTK](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer) to install the necessary packages. Ensure you add them to your PATH.


**Procedure**

1. Run `make venv && source venv/bin/activate` to install requirements, create virtual environment and activate it.
2. Run `mkdocs serve --dirtyreload`. 
3. Open your browser and navigate to http://127.0.0.1:8000/.
4. To deactivate the virtual environment afterward, run `deactivate`.

Please note that you may see slightly different results compared to our production documentation, which uses
[MkDocs Material Insiders](https://squidfunk.github.io/mkdocs-material/insiders/).

**Troubleshooting**

If you encounter issues with missing cairo-related packages, try adding the Homebrew lib path directly before running MkDocs (as described in the [troubleshooting documentation](https://t.ly/MfX6u)):

```shell
export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib
```

## Docker Image

As mentioned in the `Live Preview` section above, we have a Docker image which
is used by the CI pipeline for building the documentation site, as well as can
be leveraged during writing the documentation for live preview.

The main motivation behind the image is to allow leveraging
[MkDocs Material Insiders](https://squidfunk.github.io/mkdocs-material/insiders/)
without publishing its sources, while still allowing us to publish the source
code of our documentation.

### Updating Container Image

```shell
make docker-build
make docker-push
```

## `mike` Cookbook

You probably don't need to read this section. :)

`mike` is a build and version tool for MkDocs. It works by building the current
checkout locally and then pushing it to the appropriate directory under
the `gh-pages` branch.

BEWARE that incorporating MkDocs Material Insiders made things a bit more
complicated.
Make sure that in case you need to run `mike`, you either:

- use the Docker image, which includes MkDocs Material Insiders
- use a virtual environment created with `make mike`, which replaces
  `mkdocs-material` with the Insiders edition.

### Why Do We Have `gh-pages` on GitLab?

`mike` expects to be running on GitHub. GitHub uses the `gh-pages` branch as a
store for files being deployed to the static website. To allow `mike` function
normally:

- we have kept the `gh-pages` branch
- there is a CD/CI job in the branch, which packages up content and uploads it
  to [our hosting environment](https://ipfabric.atlassian.net/wiki/x/B4CP8w)

You can see the previous versions being saved in the `gh-pages` branch. It looks
something like this:

```none
.
├── 0.0.1
├── 0.0.2
├── 0.0.3
├── index.html
├── latest
├── main
└── versions.json
```

The directories `0.0.1`, `0.0.2`, `0.0.3` and `main` contain full builds of the
appropriate versions of the documentation. The `latest` directory contains a
redirect to the latest named version, which we have aliased as being the latest
(it is `0.0.3` in our example).

The `index.html` file in the root directory redirects to the default version
(which is `latest`).

The `versions.json` file contains information about published versions. This is
consumed by the Material Theme to render version switcher at the top of the
page.

### Release New Version of Documentation

Please be careful -- running `mike` with `--push` will result in immediate
changes in the repository (no reviews and such), as described in the steps
taken.

Let's assume that the latest visible version is `7.3` and want to release a brand new `7.5`.
The current `main` corresponds to the content of the `7.5` release. To release
it, we just need to do the following:

<!--
Keeping following lines there to ensure they are not lost until a new lines are properly tested
- tag `main` with `4.6` to mark the point in time when we have made the cut
- run `mike deploy --push --update-aliases 4.6 latest` -- this:
  - builds a static site with the release
  - moves it under the `4.6` directory at the `gh-pages` branch
  - updates the `latest` alias to point to the newly created `4.6`
  - push all commits which were made on the `gh-pages` branch to the origin

```
make mike
source venv/bin/activate
mike deploy --config-file mkdocs_insiders.yml 5.0
mike alias --update-aliases 5.0 latest
 if everything looks good, push `gh-pages`
```
-->
- Create a new release branch
- Run `make mike`
- Switch to `venv`
- Run `mike deploy` both commands as below
  - A new release branch gets its own alias, and any changes in main will apply to an upcoming unreleased version, such as 7.6.

```
git checkout -B release/7.5
make mike
source venv/bin/activate
mike deploy --config-file mkdocs_insiders.yml 7.5
mike deploy --push --update-aliases 7.5
```

### Post-Steps and Notes After New Branch Creation

#### Low Level Release Notes

The **Low Level Release Notes** should be generated for every new release.

#### Display Rules

We use a `.pages.yml` file to display and sort **Release Notes** and **Low Level Release Notes**
pages. This configuration must be version-specific for each release.

- The **Release Notes** section:
  - Should not show more than 3 the most recent release note pages by default.
  - All older versions must be grouped under a **Previous releases** section.
- The **Low Level Release Notes** section:
  - Follows similar logic to **Release Notes**.
  - However, versions are moved to **Previous releases** only based on **major version**.
  - This means that any LLRN with version `7.X` must remain outside **Previous releases** until version `8.0` is released.

#### Finalizing a Specific Version

For each finalized release version:

- Remove the `tags: ["draft"]` metadata.
- Remove the `!!! danger "Unreleased Version"` section from the release notes.

- The `latest` version marker must **only** be changed after the **General Availability (GA)** release.
- Creating a new release branch and publishing release pages does **not** imply a GA.
- Releasing new release pages corresponds to the **Early Access (EA)** stage.

#### Release Overview

The **IP Fabric Releases Overview** page must be updated accordingly to reflect the newly added version and its categorization.

- `snippets/upgrade_version_policy.md`

### Release Update to Existing Version

We use "release" branches for tracking release-specific (backported) changes.
Those follow the `release/x.y` naming, such as `release/5.0`. Just be aware that
such a branch may not exist yet as the release is fresh enough (e.g. all updates
from `main` goes to the release as well) or there were no changes necessary. :)

Check the `gh-pages` branch for the actual commit hashes used for the release
build.

For example:

```
52dcc8893 - Deployed 541d97e0d to 5.0 with MkDocs 1.3.1 and mike 1.1.2
```

means that the `541d97e0d` was deployed to version `5.0` on the website.

- Create a new branch to track your changes. Make sure that it is based on the
  appropriate release branch (or create it). In other words, the parent of the
  branch needs to be a release branch (e.g. `release/5.0`).
- Make all your changes. Push the branch to `origin`.
- Create a merge request, make sure that you appropriately set the target branch
  for it (e.g. merging from `my_5.0_update` to `release/5.0`). Never merge it
  into `main`! Make clear (e.g. in the title) that you are updating a tagged
  release.
- When merged, checkout the release branch and deploy it with `mike`:

  ```
  make mike
  source venv/bin/activate
  mike deploy --config-file mkdocs_insiders.yml --push 5.0
  ```

- agrr, profit!

### Removing Old Release

You can use `mike list` and `mike delete` to remove obsolete releases from the
website. Use with caution!

### Updating Low-Level Release Notes (LLRN) From JIRA

Script `jira_release_notes.py` will refresh all low-level
release notes from JIRA from version `7.0.0`. There are certain shortcuts, like hard-coded
configuration values. Also, check your release filtering in there to limit which
releases are actually refreshed.

To use this script, you need to export two environment variables:

- `JIRA_USER` -- your username (e.g. `first.last@ipfabric.io`)
- `JIRA_PASS` -- a token you can get from the
  [JIRA API Tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
  page

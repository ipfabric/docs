# IP Fabric Documentation Project

We are using [MkDocs](https://www.mkdocs.org/) with an excellent [Material for
MkDocs](https://squidfunk.github.io/mkdocs-material/). Last, but not least, is
[mike](https://github.com/jimporter/mike), which is a tool for building and
publishing different versions of the documentation.

> Site is currently accessible at https://docs.bobek.cz/main/

## Release process

One of the main motivations for migration towards Markdown-based documentation
is ability to follow standard development model. Thus any update to the
documentation happens as follows:

- create your "feature" branch. It is a good practice to include a ticket number
  at the beginning. For example `NIM-5808_readme`.
- do all you commits in the branch. When ready, open a merge-request in GitLab
  (also make sure, that it starts with your ticket number, correctly formatted).
- the CI/CD pipeline builds and publishes on every push to `main`.
- `mike` is then used by repository maintainers to push a new version release to
  the documentation web. (See the `mike` section below.)

## Writing documentation

### General recommendations

You can use [vale](https://github.com/errata-ai/vale) to help you keep
consistent documentation style. It keeps an eye on your choice of words, tenses,
sentence complexity and much more.

There are some great resource on how to write a good documentation out on
Interwebs. Good starting points:

- [Google's Technical Documentation Style Guide](https://developers.google.com/style)
- [Google's Technical Writing Course](https://developers.google.com/tech-writing)

### Repository layout

All the documents live under `docs` directory. Directories are used to create
sections. Please, pay attention to naming. We have opted for automated content
discovery which honors alphabetical order. Another approach would be manual
configuration with `nav` section, but that would require manual addition of
every single new page. This approach is similar in other documentation builders
(except Sphinx). You can read more at [mkdocs documentation on file
layout](https://www.mkdocs.org/user-guide/writing-your-docs/).

### Writing your documents

Documents are written in Markdown with some helpful extensions. List of enabled
extensions is at `mkdocs.yml` under `markdown_extensions` section.

- [admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/) for call outs like "example", "note", "warning" etc.
- [attr_list](https://squidfunk.github.io/mkdocs-material/reference/buttons/) for nice Buttons
- [def_list](https://squidfunk.github.io/mkdocs-material/reference/lists/#using-definition-lists) for definition lists

Please, make yourself familiar with [Material Reference Guide](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/) and [MkDocs Markdown Guide](https://www.mkdocs.org/user-guide/writing-your-docs/#writing-with-markdown).

### Live preview

You can run live preview, which is super helpful when writing / editing the
documentation. It is simple as equivalent of

```shell
virtualenv -p python3 /tmp/virtualenv && source /tmp/virtualenv/bin/activate && pip3 install -r requirements.txt && mkdocs serve
```

## `mike` cookbook

`mike` is a build and version tool for MkDocs. It works by building the current
checkout locally and then pushing it to appropriate directory under `gh-pages`
branch.

### Why do we have `gh-pages` on GitLab?

`mike` expects to be running on GitHub. GitHub uses `gh-pages` branch as a store
for files being deployed to the static website. GitLab has a different approach
and uses artifact called `public` to achieve the same. To allow `mike` function
normally, we have:

- kept `gh-pages` branch
- there is a CD/CI job in the branch, which copies content to `public` artifact
  when pushed to `gh-pages` branch.

You can see the previous versions being saved in the `dh-pages`. It looks
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

Directories `0.0.1`, `0.0.2`, `0.0.3` and `main` contains full builds of the
appropriate versions of the documentation. Directory `latest` contains redirect
to the latest named version, which we have aliased as being the latest (it is
`0.0.3` in our example).

File `index.html` in the root redirects to default version (which is `latest`).

File `versions.json` contains information about published versions. This is
consumed by the Material Theme to render version switcher at the top of the
screen.

### Release a new version of documentation

Let's assume, that we are on version `4.5` and want to release a brand new
`4.6`. Current `main` corresponds to content of `4.6` release. To release it we
just need to do the following:

- tag `main` with `4.6` to mark point in time when we have made the cut.
- run `mike deploy --push --update-aliases 4.6 latest` this
  - builds a static site with release
  - moves it under `4.6` directory at the `gh-pages` branch
  - updates alias `latest` to point to newly created `4.6`
  - push all commits which were made on `gh-pages` to the origin

### Release an update to existing version

Let's assume, that our latest version is `4.6`. But we have found a serious
issue with documentation for version `3.8` and we want to update it.

- Create a new branch from the tag, like `git switch -c update_3.8 3.8`.
- Make all your changes. Push branch to `origin`.
- Don't merge it into `main`!
- Mark the new release commit, like `git tag -f 3.8`, you need to delete
  the remote tag as well (`git push origin :v3.8`).
- Push everything to `origin` (don't forget `git push tags --all`).
- Update the released documentation with `mike deploy --push 3.8`.
- agrr, profit!

### Removing old release

You can use `mike list` and `mike delete` to remove obsolete releases from the
website. Use with caution!

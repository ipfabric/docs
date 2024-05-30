# Content Snippets

This directory contains short bits that tend to repeat throughout the site. You
can use the "snippet include" syntax to include them into your document. The
build process strictly checks for the existence of includes and will crash if a
non-existing file is included.

Please note that while markdown is correctly rendered for the included snippets,
they will **not** be included in a page's table of contents. Thus, the general
rule of thumb is not to have any headings in the snippets.

To include one snippet, use:

```
--8<-- "snippets/yourfile.md"
```

To include multiple snippets at once, use:

```
--8<--
snippets/yourfile.md
snippets/yoursecondfile.md
--8<--
```

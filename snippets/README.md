# Content snippets

This folder short bits which tend to repeat throughout the site. You can use the "snippet include syntax" to include them into your document. Build process strictly checks for existence of includes, and will crash if non-existing file is included.

Please note, that while markdown is correctly rendered for the included snippets, it will **not** be included in page table of content. Thus the general rule of thumb is not to have any headings in the snippets.

To include one snippet use

```
--8<-- "snippets/yourfile.md"
```

To include multiple snippets at once use

```
--8<--
snippets/yourfile.md
snippets/yoursecondfile.md
--8<--
```

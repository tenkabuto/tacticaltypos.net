## Site generation and serving
### Local Testing
`python3 build.py` for building local files for testing

`http-server` for testing

### Pushing to live
`python3 deploy.py` for building public files for local testing

Then copy the contents of the `public` folder into the `tacticaltypos.net` folder in my home directory, then in my Git client stage all changes, commit, and push to Github

## Added footnotes capabilities
I was able to do this by swapping out `commonmark` for `marko` in the lettersmith_py files `setup.py` and `markdowntools.py` , then commenting out the fourth line in my lettersmith project's `build.py` file:

```php
all_pages = pipe(
    (*pages, *home),
    wikidoc.content_markdown(base_url),
    # absolutize.absolutize(base_url),
)
```

If I didn't comment this out, the footnote links would link to the first page of the site.

## Site todos
- [x] Change templates to use prior site's look
- [x] Move CSS files into static and change paths
- [x] Confirm that the base_url works, or figure out what else would work
- [x] Remove dummy nav links
- [x] See if doc.modified works?
- [x] Figure out better workflow for updating to Github
	- [x] Possibly use Github actions to take in changes to source and then automatically run `deploy.py` script and have Github serve the static files
- [ ] Clean up documentation of resources that I pulled on to make the GitHub Actions => GitHub Pages thing work. Currently some notes are in [[2023-04-11]]

Additional things I'd possibly want to do:
- collect pages with YAML tags, make separate tag pages, link to tag archives from tagged page/post
- have dated pages separate from regular ones
	- dated pages have a feed
	- have these linked to in a separate backlinks area, filtered out from links from pages



## Features I want but don't know if they're possible
While I was able to install the [marko extension for tables of contents](https://marko-py.readthedocs.io/en/latest/extensions.html), I didn't know enough about how lettersmith is setup to figure out how to embed table of contents into a page template.

It'd also be really cool if someone could figure out how to link to sections of a page while keeping it Obsidian-supported.

## Other related sites
Cool notes using obsidian and lettersmith: https://ericmjl.github.io/notes/
- https://ericmjl.github.io/notes/state-of-data-science/
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
- [ ] Figure out better workflow for updating to Github
	- [ ] Possibly use Github actions to take in changes to source and then automatically run `deploy.py` script and have Github serve the static files
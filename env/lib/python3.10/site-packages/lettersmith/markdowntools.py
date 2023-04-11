from marko import Markdown
from lettersmith.html import strip_html
from lettersmith import docs as Docs
from lettersmith.func import compose


markdown = Markdown(extensions=['footnote'])
strip_markdown = compose(strip_html, markdown)
content = Docs.renderer(markdown)

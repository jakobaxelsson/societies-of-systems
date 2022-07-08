"""
Builds html files for the site from markdown. 
The source code should be placed in the source directory, and the output will be placed in the docs directory.
"""

from pathlib import Path
import shutil

import dominate
import dominate.tags as dom
from dominate.util import raw
import mistune
import yaml

class BulmaRenderer(mistune.HTMLRenderer):
    """
    A mistunes renderer which extends the HTML renderer to also include Bulma styling information.
    """    
#    pass
    def heading(self, text, level):
        return f'<h{level} class="title is-{level}">{text}</h{level}>'

html_parser = mistune.create_markdown(renderer = BulmaRenderer())

def process_file(path: Path):
    """
    Extracts directives and body of a markdown file. The directives is returned as a dictionary, and the body as a html string.

    Args:
        path (str): the name of the file.

    Returns:
        dict, str: a pair consisting of the directives as a dictionary and the body text as a html string.
    """    
    with path.open("r", encoding = "utf-8") as f: 
        text = f.read()
    _, front_matter, body = text.split("---", 2)
    directives = yaml.safe_load(front_matter)
    html = html_parser(body)
    return directives, html

# General CSS directives
css = """
img { display: block; margin-left: auto; margin-right: auto; }
h1 { text-transform: uppercase; text-align: center; }
a { color: black; text-decoration: underline; }
* { font-family: "Century Schoolbook", Century, Garamond, serif; }
"""

def create_page(path: Path, body: str):
    """
    Creates a html page containing the body text provided in the path provided. 

    Args:
        path (Path): file path to the new page.
        body (str): the html text of the body of the page.
    """
    # TODO: Add proper formating.
    with dominate.document(title = "Societies of Systems") as d:
        # Header information
        with d.head:
            dom.meta(name = "viewport", content = "width=device-width, initial-scale=1")
            dom.link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css")
            dom.link(rel = "icon", type = "image/png", sizes = "32x32", href = "/favicon-bee.png")
            with dom.style() as s:
                s += css

        # Navbar
        with dom.nav(cls = "navbar"):
            dom.a("Home", href = "/index.html", cls = "navbar-item")
            dom.a("About", href = "/about.html", cls = "navbar-item")
            dom.a("Jakob Axelsson", href = "/jakob-axelsson.html", cls = "navbar-item")

        # Banner
        with dom.div(style = "position: relative; text-align: center; color: white;"):
            dom.img(src = "/assets/banner.jpg", style = "object-fit: cover; height: 300px; width: 100%; ")
            dom.h1("Societies of Systems", 
                   style = "position: absolute; top: 60%; left: 50%; transform: translate(-50%, -50%); text-transform: uppercase;", 
                   cls = "title is-1 has-text-white")
            dom.h2("A journey into digitalization and the engineering of complex systems", 
                   style = "position: absolute; top: 85%; left: 50%; transform: translate(-50%, -50%);", 
                   cls = "subtitle is-4 has-text-white is-italic")

        # Body
        with dom.div(cls = "columns is-centered"):
            with dom.div(cls = "column is-half"):
                with dom.div(cls = "content"):
                    raw(body)
    with path.open("w") as f:
        f.write(d.render())
    print(f"Generated {path}")

if __name__ == "__main__":
    source = Path("source")
    docs = Path("docs")

    # Create the output directory structure, removing previously existing files.
    if docs.exists():
        shutil.rmtree(docs)
    shutil.copytree(source, docs, ignore = shutil.ignore_patterns("*.md"))

    # Process posts, while keeping a list of their directives to later create an index on the start page.
    posts = []
    for post_file in (source / "posts").glob("*.md"):
        directives, body = process_file(post_file)
        html_file = docs / "posts" / (post_file.stem + ".html")
        create_page(html_file, body)
        # Add the relative path to the html file to the directives dictionary for later use in links.
        directives["href"] = html_file.relative_to(docs)
        posts.append(directives)

    # Create non-post pages
    for page in [source / "about.md", source / "jakob-axelsson.md"]:
        _, body = process_file(page)
        html_file = docs / (page.stem + ".html")
        create_page(html_file, body)

    # Create index page, containing a list of all posts by reverse dates
    _, body = process_file(source / "index.md")
    posts.sort(key = lambda d : d["date"], reverse = True)
    for post in posts:
        link = dom.p(dom.a(f"{post['title']} ({post['date'][:10]})", href = post["href"]))
        body += link.render()
    create_page(docs / "index.html", body)
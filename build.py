"""
Builds html files for the site from markdown. 
The source code should be placed in the source directory, and the output will be placed in the docs directory.
Also generates CSS from SASS.
"""

from pathlib import Path
import shutil

import dominate
import dominate.tags as dom
from dominate.util import raw
import mistune
import sass
import yaml

html_parser = mistune.create_markdown()

def process_file(path: Path):
    """
    Extracts directives and body of a markdown file. 
    The page is returned as a dictionary, containing the directives and the body as a html string.

    Args:
        path (Path): the name of the file.

    Returns:
        dict: the page as a dictionary, with the directives and the body text as a html string.
    """    
    with path.open("r", encoding = "utf-8") as f: 
        text = f.read()
    _, front_matter, body = text.split("---", 2)
    page = yaml.safe_load(front_matter)
    page["body"] = html_parser(body)
    page["path"] = path
    return page

def create_page(path: Path, page):
    """
    Creates a html page containing the body text provided in the path provided. 

    Args:
        path (Path): file path to the new page.
        page (dict): directives and page body.
    """
    with dominate.document(title = "Societies of Systems") as d:
        # Header information
        with d.head:
            dom.meta(name = "viewport", content = "width=device-width, initial-scale=1")
            dom.link(rel = "stylesheet", href = "/css/style.css")
            dom.link(rel = "icon", type = "image/png", sizes = "32x32", href = "/favicon-bee.png")

        # Add page type as class to body
        d.body["class"] = page["layout"]

        with dom.header(cls = "header"):
            # Navbar
            with dom.nav(cls = "navbar"):
                dom.a("Home", href = "/index.html", cls = "navbar-item")
                dom.a("About", href = "/about.html", cls = "navbar-item")
                dom.a("Jakob Axelsson", href = "/jakob-axelsson.html", cls = "navbar-item")
            dom.h1("Societies of Systems", cls = "site-title")
            dom.h2("A journey into digitalization and the engineering of complex systems", cls = "site-subtitle")

        # Body
        with dom.div(cls = "content"):
            dom.h1(page["title"])
            if "date" in page:
                dom.h3(f"Posted on {page['date']}", cls = "post-date")
            raw(page["body"])
    with path.open("w") as f:
        f.write(d.render())
    print(f"Generated {path} of page type {page['layout']}")


if __name__ == "__main__":
    source = Path("source")
    docs = Path("docs")

    # Create the output directory structure, removing previously existing files.
    if docs.exists():
        shutil.rmtree(docs)
    shutil.copytree(source, docs, ignore = shutil.ignore_patterns("*.md", "sass"))

    # Compile SASS files to CSS
    if (source / "sass").exists():
        sass.compile(dirname = (source / "sass", docs / "css"))
        print(f"Generated {docs / 'css'}")
    
    # Process posts, while keeping a list of their pages to later create an index on the start page.
    posts = []
    for page_file in (source / "posts").glob("*.md"):
        page = process_file(page_file)
        html_file = (docs / "posts" / page_file.name).with_suffix(".html")
        create_page(html_file, page)
        posts.append(page)

    # Create non-post pages
    for page_file in [source / "about.md", source / "jakob-axelsson.md"]:
        page = process_file(page_file)
        html_file = (docs / page_file.name).with_suffix(".html")
        create_page(html_file, page)

    # Create index page, containing a list of all posts by reverse dates
    page = process_file(source / "index.md")
    posts.sort(key = lambda d : d["date"], reverse = True)
    for post in posts:
        link = dom.p(dom.a(f"{post['title']} ({post['date']})", href = post["path"].relative_to(source).with_suffix(".html")))
        page["body"] += link.render()
    create_page(docs / "index.html", page)
"""
Builds html files for the site from markdown. 
The source code should be placed in the source directory, and the output will be placed in the docs directory.
It also generates CSS from SASS, and an RSS feed of all posts.
"""

import datetime
from pathlib import Path
import shutil

import dominate
import dominate.tags as dom
from dominate.util import raw, text
import mistune
import rfeed
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
            dom.meta(charset = "utf-8")
            dom.link(rel = "stylesheet", href = "/css/style.css")
            dom.link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")
            dom.link(rel = "icon", type = "image/png", sizes = "32x32", href = "/assets/favicon-bee.png")
            dom.script(type = "text/javascript", src = "/assets/responsiveness.js")

        # Add page type as class to body
        d.body["class"] = page["layout"]

        with dom.header(cls = "header"):
            # Navbar
            with dom.nav(cls = "navbar"):
                with dom.a(href = "javascript:void(0);", cls = "icon", onclick = "toggle_menu()"):
                    dom.i(cls = "fa fa-bars")
                dom.a("Home", href = "/index.html", cls = "navbar-item")
                dom.a("About", href = "/about.html", cls = "navbar-item")
                dom.a("Jakob Axelsson", href = "/jakob-axelsson.html", cls = "navbar-item")
            with dom.div(cls = "header-text"):
                dom.h1("Societies of Systems", cls = "site-title")
                dom.h2("A journey into digitalization and the engineering of complex systems", cls = "site-subtitle")

        # Body
        with dom.div(cls = "content"):
            dom.h1(page["title"])
            if "date" in page:
                dom.h3(f"Posted on {page['date']}", cls = "post-date")
            raw(page["body"])

        # Footer
        with dom.footer(cls = "footer"):
            text("© Jakob Axelsson")
            with dom.a(href = "/rss.xml"):
                dom.i(cls = "fa fa-rss-square", style = "font-size: 22px; color: orange")

    path.write_text(d.render(), encoding = "utf-8")
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

    # Create RSS feed
    path = docs / "rss.xml"
    items = []
    for post in posts:
        item = rfeed.Item(
            title = post["title"],
            link = post["path"].relative_to(source).with_suffix(".html"),
            description = post["description"],
            author = "Jakob Axelsson",
            guid = rfeed.Guid(""),
            pubDate = datetime.datetime.fromisoformat(str(post["date"]))
        )
        items.append(item)
    feed = rfeed.Feed(
        title = "Societies of systems",
        link = "",
        description = "Societies of systems: A journey into digitalization and the engineering of complex systems",
        # Use the date of the most recent post as the last build date.
        lastBuildDate = datetime.datetime.fromisoformat(str(posts[0]["date"])),
        items = items
    )
    path.write_text(feed.rss(), encoding = "utf-8")
    print(f"Generated {path}")
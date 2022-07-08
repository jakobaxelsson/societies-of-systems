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

html_parser = mistune.create_markdown()

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

def create_page(path: Path, body: str):
    """
    Creates a html page containing the body text provided in the path provided. 

    Args:
        path (Path): file path to the new page.
        body (str): the html text of the body of the page.
    """
    # TODO: Add proper formating.
    with dominate.document() as d:
        dom.p(dom.a("Home", href = "/index.html"))
        dom.p(dom.a("About", href = "/about.html"))
        dom.p(dom.a("Jakob Axelsson", href = "/jakob-axelsson.html"))
        dom.p(dom.img(src = "/assets/banner.jpg"))
        raw(body)
    with path.open("w") as f:
        f.write(d.render())
    print(f"Generated {path}")

def change_suffix(path: Path, suffix: str) -> str:
    """
    Changes the suffix of the given filename.

    Args:
        path (Path): the file path, including old suffix.
        suffix (str): the new suffix.

    Returns:
        str: the filename with the new suffix.
    """
    return path.parent / (path.stem + "." + suffix)


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
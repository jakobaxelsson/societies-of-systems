# Societies of Systems

This is the repository for the Societies of Systems blog, for hosting on Github pages. It is still under development.

## Building the site

The current version contains a custom build script. It is executed using `python build.py`. 

The script converts all Markdown files to HTML, and also compiles the SASS files to CSS. 
The input files are in the `source` directory.
The result will be in the `docs` directory, which contains all that is needed for the actual website.
The contents of the `docs` directory should never be edited manually, since changes will be overwritten in subsequent builds.

The Markdown files start with a preamble, containing some meta information about the page. This is written in YAML.

## Local testing

The result can be tested locally using `python -m http.server --directory docs`. The pages can then be accessed from the browser on the address `127.0.0.1:8000`.

## Github pages information

The site is intended for publishing at Github pages. This requires the following special files:

- `.nojekyll`: Tells Github to publish the provided HTML files, rather than to try to compile it using Jekyll.
- `source/CNAME`: Tells Github the domain name where the site should be published.
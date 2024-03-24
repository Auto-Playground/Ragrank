import os
import sys

sys.path.insert(0, os.path.abspath("."))


# -- Project information --------
project = "Ragrank API documentation"
copyright = "2024, Izam Mohammed"
author = "Izam Mohammed"
release = "0.0.1"


# -- General configuration ---------

extensions = [
    "sphinx_design",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary"
]

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
# html_static_path = ["_static"]

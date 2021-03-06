# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import importlib

sys.path.insert(0, os.path.abspath(".."))

# mock dependencies to avoid installing them all just to build the configuration

from unittest.mock import Mock

# maybe these are important
MOCK_MODULES = [
    "yaml",
    "numpy",
    "PIL",
    "pandas",
    "matplotlib",
    "tensorflow",
    "torch",
    "skimage",
    "wandb",
    "flask",
    "jsonschema",
    "PyQt5.QtWidgets",
    "PyQt5",
    "PyQt5.QtWidgets.QApplication",
    "PyQt5.QtWidgets.QFileDialog",
    "PyQt5.QtWidgets.QTableWidgetItem",
    "PyQt5.QtWidgets.QTableWidget",
    "PyQt5.QtWidgets.QAbstractItemView",
    "PyQt5.QtWidgets.QMenuBar",
    "PyQt5.QtWidgets.QAction",
    "flask_wtf",
    "wtforms",
    "wtforms.validators",
]

for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = Mock()


def run_apidoc(app):
    """Generate API documentation"""
    import better_apidoc

    better_apidoc.APP = app
    better_apidoc.main(
        [
            "better-apidoc",
            "-a",
            "-M",
            "-t",
            os.path.join(".", "templates"),
            "--force",
            "--no-toc",
            "--separate",
            "--ext-autodoc",
            "--ext-coverage",
            "-o",
            os.path.join(".", "source", "source_files/"),
            os.path.join("..", "project/"),
        ]
    )


def setup(app):
    app.connect("builder-inited", run_apidoc)


# -- Project information -----------------------------------------------------

project = "CoronaHackathon"
copyright = "2020, #wir"
author = "wir"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

# html_static_path = ['_static']

autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
}

exclude_patterns = ["_build"]

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False

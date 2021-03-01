# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx_rtd_theme

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Adventure'
copyright = '2020-2021, KyoriPowered'
author = 'KyoriPowered'

# The short X.Y version
version = '4.4.0'

# The full version, including alpha/beta/rc tags
release = version

if release.endswith('-SNAPSHOT'):
    tags.add('draft')

rst_prolog = """
.. danger::

    The Adventure docs are currently a **work in progress**. Some areas may have limited coverage or may not be entirely up to date.
    Feel free to join our discord at `<https://discord.gg/MMfhJ8F>`_ if you have any questions.

"""



# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'sphinx_rtd_theme',
  'sphinx_tabs.tabs'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# General style

smartquotes = True
language='en'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_style = 'css/kyori.css'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_show_sourcelink = False
html_copy_source = False
html_sidebars = {
    '**': ['logo-text.html',
          'globaltoc.html',
          'localtoc.html',
          'searchbox.html']
}

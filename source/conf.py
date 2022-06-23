# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
from pathlib import Path

project = 'Adventure'
copyright = '2020-2022 KyoriPowered'
author = 'KyoriPowered'

# The short X.Y version
version = '4.11.0'

# The latest version of adventure-platform builds
platformVersion = '4.1.1'
fabricPlatformVersion = '5.3.1'

# The full version, including alpha/beta/rc tags
release = version

if release.endswith('-SNAPSHOT'):
    tags.add('draft')

rst_prolog = f"""
.. danger::

    The Adventure docs are currently a **work in progress** and supplement the `Javadocs <https://jd.adventure.kyori.net>`_.
    Some areas may have limited coverage or may not be entirely up to date.
    Feel free to join our `Discord <https://discord.gg/MMfhJ8F>`_ if you have any questions.

.. |version| replace:: {version}

.. |platform_version| replace:: {platformVersion}

.. |fabric_platform_version| replace:: {fabricPlatformVersion}

.. role:: mm(code)
    :language: minimessage
    :class: highlight

.. role:: java(code)
    :language: java
    :class: highlight

"""

if 'GITHUB_REF' in os.environ:
    ref = os.environ['GITHUB_REF']
    if ref.startswith("refs/pull/"):
        pr_number = ref[len("refs/pull/"):-len("/merge")]
        rst_prolog += f"""
.. caution::

    This version of the Adventure documentation has been built as a preview of pull request :github:`adventure-docs#{pr_number}`, and has not been reviewed.

    Please consult the pull request to view any discussion and existing reviews.
"""
    else:
        html_baseurl = "https://docs.adventure.kyori.net/"

# -- General configuration ---------------------------------------------------

# Add local extensions
sys.path.append(os.path.abspath("./_ext"))

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'sphinx_design',
  'sphinx_substitution_extensions',
  'sphinx_github_changelog',
  'sphinx_reredirects',
  'sphinx_github_role',
  'sphinx_copybutton',
  'minimessage_hl',
  'adventure_docs_extensions'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_ext']


# General style

smartquotes = True
language = 'en'

pygments_style = 'friendly'
pygments_dark_style = 'dracula'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ["button/button.css"]

html_theme_options = {
    'light_css_variables': {
        "color-brand-primary": "#2f2850",
        "color-brand-content": "#6355aa",
    },
    'dark_css_variables': {
        "color-brand-primary": "#b597d3",
        "color-brand-content": "#7767c9",
    },
    'sidebar_hide_name': True
}

html_title = f'Adventure Documentation (v{version})'
html_show_sourcelink = False
html_copy_source = False
html_favicon = '_static/favicon.ico'
html_logo = '_static/logo.png'

# sphinx-reredirects
redirects = {
    'minimessage': 'minimessage/'
}

# sphinx-github-role
github_default_org_project = ('KyoriPowered', 'adventure')

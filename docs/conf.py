# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import re
sys.path.insert(0, os.path.abspath('..\\.'))


# -- Project information -----------------------------------------------------

project = 'TMIP-EMAT'
copyright = ''
html_show_copyright = False
author = 'Cambridge Systematics, Inc.'

def version(path):
    """Obtain the packge version from a python file e.g. pkg/__init__.py
    See <https://packaging.python.org/en/latest/single_source_version.html>.
    """
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, path), encoding='utf-8') as f:
        version_file = f.read()
    version_match = re.search(r"""^__version__ = ['"]([^'"]*)['"]""",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

VERSION = version('../emat/__init__.py')

# The short X.Y version
version = VERSION

from datetime import datetime
# The full version, including alpha/beta/rc tags
release = '{}, {}'.format(VERSION, datetime.today().strftime("%B %Y"))


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinxcontrib.restbuilder',
    'nbsphinx',
    'jupyter_sphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**ipynb_checkpoints', '**junk']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

intersphinx_mapping = {
	'python': ('https://docs.python.org/3.7/', None),
	'numpy': ('https://docs.scipy.org/doc/numpy/', None),
	'pandas': ('http://pandas.pydata.org/pandas-docs/stable/', None),
	'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
	'sklearn': ('https://scikit-learn.org/stable/', None),
    'ema_workbench': ('https://emaworkbench.readthedocs.io/en/latest/', None),
    'conda': ('https://docs.conda.io/projects/conda/en/latest/', None),
}


rst_prolog = """

.. warning:: This is **DRAFT** documentation under development.  The interfaces
    documented are shown for illustration and are not guaranteed to be stable 
    in future releases of TMIP-EMAT.
    
    The views expressed in this draft documentation do not necessarily 
    represent the opinions of FHWA, and do not constitute an endorsement, 
    recommendation, or specification by FHWA.

"""

nbsphinx_timeout = 300

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'

import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {}

html4_writer=True  # see https://github.com/readthedocs/sphinx_rtd_theme/issues/766

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = "_static/logo.png"

html_style = 'css/tmip_emat.css'

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'TMIP-EMATdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'TMIP-EMAT.tex', 'TMIP-EMAT Documentation',
     'Cambridge Systematics, Inc.', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'tmip-emat', 'TMIP-EMAT Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'TMIP-EMAT', 'TMIP-EMAT Documentation',
     author, 'TMIP-EMAT', 'One line description of project.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

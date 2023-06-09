# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../..'))
sys.path.append(os.path.abspath('extensions'))

project = 'weatherly'
copyright = '2023, konradsic'
author = 'konradsic'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinxcontrib_trio',
    'sphinx_copybutton',
    'attributetable',
]

templates_path = ['_templates']
exclude_patterns = []

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_rtype = False
autodoc_member_order = 'groupwise'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_css_files = ['style.css']
html_js_files = ['custom.js']

html_theme_options = {
    'home_page_in_toc': True,
    'show_navbar_depth': 1,
    'show_toc_level': 2,
    'repository_url': 'https://github.com/konradsic/weatherly',
    'use_repository_button': True,
    'logo': {
        'image_light': 'weatherly_banner_light.png',
        'image_dark': 'weatherly_banner.png',
    }
}

html_sidebars = {
    '**': [
        'navbar-logo.html',
        'localtoc.html'
    ]
}

intersphinx_mapping = {'py': ('https://docs.python.org/3', None),
                       'requests': ('https://requests.readthedocs.io/en/latest/', None),}
html_favicon = './images/weatherly_icon.ico'
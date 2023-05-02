# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("../.."))
sys.path.append(os.path.abspath("extensions"))

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
    'attributetable',
]

templates_path = ['_templates']
exclude_patterns = []

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_rtype = False
autodoc_member_order = "groupwise"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_css_files = ["css/style.css"]
html_js_files = ["js/custom.js"]

html_theme_options = {
    'home_page_in_toc': True,
    'show_navbar_depth': 2,
    'show_toc_level': 2,
}

intersphinx_mapping = {"py": ("https://docs.python.org/3", None)}
pygments_style = "zenburn"
# styles: ['default', 'emacs', 'friendly', 'friendly_grayscale', 'colorful', 'autumn', 'murphy', 'manni', 'material', 'monokai', 
# 'perldoc', 'pastie', 'borland', 'trac', 'native', 'fruity', 'bw', 
#'vim', 'vs', 'tango', 'rrt', 'xcode', 'igor', 'paraiso-light', 'paraiso-dark', 'lovelace', 'algol', 'algol_nu', '
# arduino', 'rainbow_dash', 'abap', 'solarized-dark', 'solarized-light', 'sas', 'staroffice', 'stata', 'stata-light', 'stata-dark', 
# 'inkpot', 'zenburn', 'gruvbox-dark', 'gruvbox-light', 'dracula', 'one-dark', 'lilypond', 'nord', 'nord-darker', 'github-dark', 
#'a11y-dark', 'a11y-high-contrast-dark', 'a11y-high-contrast-light', 'a11y-light', 'blinds-dark', 'blinds-light', 'github-dark', 
# 'github-dark-colorblind', 'github-dark-high-contrast', 'github-light', 'github-light-colorblind', 'github-light-high-contrast', 
# 'gotthard-dark', 'gotthard-light', 'greative', 'pitaya-smoothie']
pygments_dark_style = "zenburn"
html_favicon = "./images/weatherly_icon.ico"
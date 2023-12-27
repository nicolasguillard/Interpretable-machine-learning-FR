# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Interpretable Machine Learning - FR translation'
copyright = '2023, Christoph Molnar - Trad: Nicolas Guillard'
author = 'Christoph Molnar - Trad: Nicolas Guillard'
release = '1.0.0'

# -- General configuration ---------------------------------------------------extensions = ['myst_parser']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------

html_theme = 'pyramid'
html_static_path = ['_static']

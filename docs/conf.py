# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
# -- Project information -----------------------------------------------------
import sphinx.domains.python
from sphinx.locale import _, __




project = 'Farming Simulator Modding Documentation'
copyright = '2020, marsfan'
author = 'marsfan'



# -- General configuration ---------------------------------------------------

# Main page for the documentation
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.todo"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'sticky_navigation': True,
    'navigation_depth': -1,
    'titles_only': True,
    'collapse_navigation': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Configuration options for sphinx.ext.todo--------------------------------
todo_include_todos = True

# Create custom directives for the XML documentation.
# This will allow us to use the terms that XML files use. Specifically element and attribute.
# Ideally I would write an whole new custom domain just for XML and XSD files, but I don't know how to do that
# So instead I just inherited from PyClassLike from the default Python domain



class element(sphinx.domains.python.PyClasslike):
    pass

element.doc_field_types.append(
    sphinx.domains.python.PyTypedField('attribute', label=_('Attributes'),
                 names=('attrib', 'attr', 'attribute'),
                 typerolename='class', typenames=('attribtype'),
                 can_collapse=True),
)



def setup(app):
    app.add_directive('element', element)


import sphinx_rtd_theme

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages']

templates_path = ['templates']
exclude_patterns = ['build']
project = 'CatKit'
source_suffix = ['.rst']
master_doc = 'index'
copyright = '2018, CatKit-developers'
default_role = 'math'
pygments_style = 'sphinx'
modindex_common_prefix = ['catkit.']
autoclass_content = 'both'

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['static']
html_last_updated_fmt = '%a, %d %b %Y %H:%M:%S'

version = '0.4'
release = '0.4.3'

intersphinx_mapping = {'python': ('https://docs.python.org/3.6', None)}

extensions = ['sphinx.ext.napoleon']
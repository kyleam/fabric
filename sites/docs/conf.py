# Obtain shared config values
import os, sys
from os.path import abspath, join, dirname
sys.path.append(abspath(join(dirname(__file__), '..')))
sys.path.append(abspath(join(dirname(__file__), '..', '..')))
from shared_conf import *

# Enable autodoc, intersphinx
extensions.extend(['sphinx.ext.autodoc', 'sphinx.ext.intersphinx'])

# Autodoc settings
autodoc_default_flags = ['members', 'special-members']

# Default is 'local' building, but reference the public WWW site when building
# under RTD.
target = join(dirname(__file__), '..', 'www', '_build')
if os.environ.get('READTHEDOCS') == 'True':
    target = 'http://www.fabfile.org/'
www = (target, None)
# Ditto Invoke
target = join(
    dirname(__file__),
    '..', '..', '..',
    'invoke', 'sites', 'docs', '_build'
)
if os.environ.get('READTHEDOCS') == 'True':
    target = 'http://docs.pyinvoke.org/'
invoke = (target, None)
# Intersphinx connection to stdlib + www site
intersphinx_mapping.update({
    'www': www,
})

# Sister-site links to WWW
html_theme_options['extra_nav_links'] = {
    "Main website": 'http://www.fabfile.org',
}

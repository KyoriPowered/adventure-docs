#!/usr/bin/env python3

from sphinx.application import Sphinx
import pygments.lexers
import pygments.lexers._mapping
from docutils import nodes
from docutils.parsers.rst.roles import code_role


def setup(app: Sphinx):
    # Hack to inject our lexer, without having to produce a proper package (this should happen at a later date)
    pygments.lexers._mapping.LEXERS['minimessage'] = ('minimessage_hl.lexer', 'MiniMessage component', ('minimessage', 'mm'), ('*.mm',), ())
    pygments.lexers.find_lexer_class('MiniMessage component') # update the cache

    #app.add_role('mm', _mm_role)

    # Register an interpreted text role for inline syntax highlighting
    return {
        'parallel_read_safe': True
    }

def _mm_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    options['language'] = 'minimessage'
    return code_role(name, rawtext, text, lineno, inliner, options, content)


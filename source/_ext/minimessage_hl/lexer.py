#!/usr/bin/env python3

from pygments.lexer import RegexLexer
from pygments.token import *

__all__ = ['MiniMessageLexer']

_escape = r"""\\<>'"]"""

class MiniMessageLexer(RegexLexer):
    name = 'MiniMessage component'
    aliases = ['minimessage', 'mm']
    filenames = []

    tokens = {
        'root': [
            (r'[^<]+', Literal),
            (r'\\<', Escape),
            (r'<', Name.Tag, 'tag')
        ],
        'tag': [
            (r'\\>', Escape),
            (r'>', Name.Tag, '#pop'),
            (r':', Name.Tag, 'tag_options'),
            (r'[^>:\'"]+', Name.Tag)
        ],
        'tag_options': [
            (r'\\>', Escape),
            (r':', Name.Tag),
            (r'>', Name.Tag, '#pop:2'),
            (r"'", String.Single, 'string_single'),
            (r'"', String.Double, 'string_double'),
            (r'[^>:\'"]+', Name.Attribute),
        ],
        'string_single': [
            (r"\\[']", String.Escape),
            (r"'", String.Single, '#pop'),
            (r"(?:\\[^']|[^'])+", String.Single)
        ],
        'string_double': [
            (r'\\["]', String.Escape),
            (r'"', String.Double, '#pop'),
            (r'(?:\\[^"]|[^"])+', String.Double)
        ]
    }
#!/usr/bin/env python3
# This file is part of adventure-docs, licensed under the MIT License.
#
# Copyright (c) 2017-2022 KyoriPowered
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import re
from sphinx.application import Sphinx
from docutils.parsers.rst import nodes

def setup(app: Sphinx):
    app.add_role("mojira", mojira_role)

_issue_regex = re.compile(r'[A-Z]+-[1-9][0-9]*')
_mojira_url = "https://bugs.mojang.com/browse/"

def mojira_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    if not _issue_regex.fullmatch(text):
        msg = inliner.reporter.error(f'Issue number must be in the format PROJECT-1234, but {text} was given instead', line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]

    ref = _mojira_url + text
    
    node = nodes.reference(rawtext, text, refuri=ref, **options)

    return [node], []

# -*- coding: utf-8 -*-
"""
    RSpec lexer
    ~~~~~~~~~~~

    Pygments lexer for Ruby + RSpec.

    :copyright: Copyright 2012 Hugo Maia Vieira
    :license: BSD, see LICENSE for details.
"""

from pygments.lexers.agile import RubyLexer
from pygments.token import Name, Keyword

class RspecLexer(RubyLexer):
    name = 'RSpec'
    aliases = ['rspec']
    filenames = ['*.rspec'] # just to have one if you whant to use

    EXTRA_KEYWORDS = ['describe',  'it', 'feature', 'scenario', 'background',
                     'within']

    def get_tokens_unprocessed(self, text):
        for index, token, value in RubyLexer.get_tokens_unprocessed(self, text):
            if token is Name and value in self.EXTRA_KEYWORDS:
                yield index, Keyword, value
            else:
                yield index, token, value
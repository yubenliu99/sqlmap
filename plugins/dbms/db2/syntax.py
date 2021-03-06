#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from plugins.generic.syntax import Syntax as GenericSyntax

class Syntax(GenericSyntax):
    @staticmethod
    def escape(expression, quote=True):
        """
        >>> Syntax.escape("SELECT 'abcdefgh' FROM foobar")
        'SELECT CHR(97)||CHR(98)||CHR(99)||CHR(100)||CHR(101)||CHR(102)||CHR(103)||CHR(104) FROM foobar'
        """

        def escaper(value):
            return "||".join("CHR(%d)" % ord(_) for _ in value)

        return Syntax._escape(expression, quote, escaper)

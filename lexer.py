import re

class Lexer:
    def __init__(self, input_code):
        self.input_code = input_code
        self.tokens = []
        self.token_regex = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in [
            ('IF', r'\bif\b'),
            ('ELSE', r'\belse\b'),
            ('WHILE', r'\bwhile\b'),
            ('DEF', r'\bdef\b'),
            ('RETURN', r'\breturn\b'),
            ('NUMBER', r'\d+'),
            ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('OP', r'[+\-*/<>]'),  # Include arithmetic and comparison operators
            ('ASSIGN', r'='),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('LBRACE', r'\{'),
            ('RBRACE', r'\}'),
            ('COMMA', r','),
            ('SEMICOLON', r';'),
            ('WHITESPACE', r'\s+'),
        ]))

    def tokenize(self):
        line_number = 1
        line_start = 0
        for match in self.token_regex.finditer(self.input_code):
            kind = match.lastgroup
            value = match.group()
            column = match.start() - line_start + 1
            if kind != 'WHITESPACE':
                self.tokens.append((kind, value, line_number, column))
            if '\n' in value:  # Handle line breaks
                line_number += 1
                line_start = match.end()
        return self.tokens

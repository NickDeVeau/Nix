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
            ('PRINT', r'\bprint\b'),  # Add 'PRINT' keyword
            ('NUMBER', r'\d+'),
            ('STRING', r'"[^"]*"|\'[^\']*\''),  # Add support for single-quoted strings
            ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('ASSIGN', r'='),  # Ensure ASSIGN is identified before OP
            ('OP', r'[+\-*/<>!=]'),  # Include '!' for '!=' operator
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('LBRACE', r'\{'),
            ('RBRACE', r'\}'),
            ('COMMA', r','),
            ('SEMICOLON', r';'),
            ('WHITESPACE', r'\s+'),
            ('UNKNOWN', r'.'),  # Catch-all for unknown characters
        ]))

    def tokenize(self):
        line_number = 1
        line_start = 0
        for match in self.token_regex.finditer(self.input_code):
            kind = match.lastgroup
            value = match.group()
            column = match.start() - line_start + 1
            if kind == 'WHITESPACE':
                if '\n' in value:  # Handle line breaks
                    line_number += value.count('\n')
                    line_start = match.end()
                continue  # Skip whitespace
            elif kind == 'UNKNOWN':
                raise SyntaxError(f"Unknown character '{value}' at line {line_number}, column {column}")
            else:
                self.tokens.append((kind, value, line_number, column))
        return self.tokens

import unittest
from lexer import Lexer

class TestLexer(unittest.TestCase):
    def test_basic_tokens(self):
        code = "x = 10;"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        self.assertEqual(tokens, [
            ('IDENTIFIER', 'x', 1, 1),
            ('ASSIGN', '=', 1, 3),
            ('NUMBER', '10', 1, 5),
            ('SEMICOLON', ';', 1, 7)
        ])

    def test_arithmetic_tokens(self):
        code = "x = 5 + 3 * 2;"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        self.assertEqual(tokens, [
            ('IDENTIFIER', 'x', 1, 1),
            ('ASSIGN', '=', 1, 3),
            ('NUMBER', '5', 1, 5),
            ('OP', '+', 1, 7),
            ('NUMBER', '3', 1, 9),
            ('OP', '*', 1, 11),
            ('NUMBER', '2', 1, 13),
            ('SEMICOLON', ';', 1, 14)
        ])

    def test_if_tokens(self):
        code = "if (x > 3) { y = 10; } else { y = 20; }"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        self.assertEqual(tokens, [
            ('IF', 'if', 1, 1),
            ('LPAREN', '(', 1, 4),
            ('IDENTIFIER', 'x', 1, 5),
            ('OP', '>', 1, 7),
            ('NUMBER', '3', 1, 9),
            ('RPAREN', ')', 1, 10),
            ('LBRACE', '{', 1, 12),
            ('IDENTIFIER', 'y', 1, 14),
            ('ASSIGN', '=', 1, 16),
            ('NUMBER', '10', 1, 18),
            ('SEMICOLON', ';', 1, 20),
            ('RBRACE', '}', 1, 22),
            ('ELSE', 'else', 1, 24),
            ('LBRACE', '{', 1, 29),
            ('IDENTIFIER', 'y', 1, 31),
            ('ASSIGN', '=', 1, 33),
            ('NUMBER', '20', 1, 35),
            ('SEMICOLON', ';', 1, 37),
            ('RBRACE', '}', 1, 39)
        ])

    def test_while_tokens(self):
        code = "while (x < 3) { x = x + 1; }"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        self.assertEqual(tokens, [
            ('WHILE', 'while', 1, 1),
            ('LPAREN', '(', 1, 7),
            ('IDENTIFIER', 'x', 1, 8),
            ('OP', '<', 1, 10),
            ('NUMBER', '3', 1, 12),
            ('RPAREN', ')', 1, 13),
            ('LBRACE', '{', 1, 15),
            ('IDENTIFIER', 'x', 1, 17),
            ('ASSIGN', '=', 1, 19),
            ('IDENTIFIER', 'x', 1, 21),
            ('OP', '+', 1, 23),
            ('NUMBER', '1', 1, 25),
            ('SEMICOLON', ';', 1, 26),
            ('RBRACE', '}', 1, 28)
        ])

    def test_function_tokens(self):
        code = "def add(a, b) { return a + b; }"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        self.assertEqual(tokens, [
            ('DEF', 'def', 1, 1),
            ('IDENTIFIER', 'add', 1, 5),
            ('LPAREN', '(', 1, 8),
            ('IDENTIFIER', 'a', 1, 9),
            ('COMMA', ',', 1, 10),
            ('IDENTIFIER', 'b', 1, 12),
            ('RPAREN', ')', 1, 13),
            ('LBRACE', '{', 1, 15),
            ('RETURN', 'return', 1, 17),
            ('IDENTIFIER', 'a', 1, 24),
            ('OP', '+', 1, 26),
            ('IDENTIFIER', 'b', 1, 28),
            ('SEMICOLON', ';', 1, 29),
            ('RBRACE', '}', 1, 31)
        ])

if __name__ == "__main__":
    unittest.main()

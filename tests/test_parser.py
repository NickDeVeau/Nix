import unittest
from lexer import Lexer
from parser import Parser

class TestParser(unittest.TestCase):
    def test_arithmetic_expression(self):
        code = "x = 5 + 3 * 2;"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        expected_ast = [
            ('assign', 'x', ('binary', '+', ('number', '5'), ('binary', '*', ('number', '3'), ('number', '2'))))
        ]
        self.assertEqual(ast, expected_ast)

    def test_if_statement(self):
        code = """
        if (x > 3) {
            y = 10;
        } else {
            y = 20;
        }
        """
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        expected_ast = [
            ('if', ('binary', '>', ('identifier', 'x'), ('number', '3')),
                [('assign', 'y', ('number', '10'))],
                [('assign', 'y', ('number', '20'))])
        ]
        self.assertEqual(ast, expected_ast)

    def test_while_statement(self):
        code = """
        while (x < 3) {
            x = x + 1;
        }
        """
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        expected_ast = [
            ('while', ('binary', '<', ('identifier', 'x'), ('number', '3')),
                [('assign', 'x', ('binary', '+', ('identifier', 'x'), ('number', '1')))])
        ]
        self.assertEqual(ast, expected_ast)

    def test_function_declaration(self):
        code = """
        def add(a, b) {
            return a + b;
        }
        """
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        expected_ast = [
            ('function', 'add', ['a', 'b'],
                [('return', ('binary', '+', ('identifier', 'a'), ('identifier', 'b')))])
        ]
        self.assertEqual(ast, expected_ast)

    def test_function_call(self):
        code = "x = add(2, 3);"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        expected_ast = [
            ('assign', 'x', ('call', 'add', [('number', '2'), ('number', '3')]))
        ]
        self.assertEqual(ast, expected_ast)

if __name__ == "__main__":
    unittest.main()

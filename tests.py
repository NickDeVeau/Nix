import unittest
from nix.lexer import Lexer
from nix.parser import Parser
from nix.executor import Executor

class TestInterpreter(unittest.TestCase):
    def test_arithmetic(self):
        code = "x = 5 + 3 * 2;"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        executor = Executor(ast)
        executor.execute()
        self.assertEqual(executor.variables['x'], 11)

    def test_conditionals(self):
        code = """
        x = 5;
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
        executor = Executor(ast)
        executor.execute()
        self.assertEqual(executor.variables['y'], 10)

    def test_loops(self):
        code = """
        x = 0;
        while (x < 3) {
            x = x + 1;
        }
        """
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        executor = Executor(ast)
        executor.execute()
        self.assertEqual(executor.variables['x'], 3)

    def test_functions(self):
        code = """
        def add(a, b) {
            return a + b;
        }
        x = add(2, 3);
        """
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        executor = Executor(ast)
        executor.execute()
        self.assertEqual(executor.variables['x'], 5)

if __name__ == '__main__':
    unittest.main()
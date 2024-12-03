
import unittest
from lexer import Lexer
from parser import Parser
from executor import Executor

class TestExecutor(unittest.TestCase):
    def test_arithmetic_execution(self):
        code = "x = 5 + 3 * 2;"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        executor = Executor(ast)
        executor.execute()
        self.assertEqual(executor.variables['x'], 11)

    def test_if_execution(self):
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

    def test_while_execution(self):
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

    def test_function_execution(self):
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

if __name__ == "__main__":
    unittest.main()

import sys
from lexer import Lexer
from nix.parser import Parser
from nix.executor import Executor

def main():
    if len(sys.argv) != 2:
        print("Usage: nixlang <file.nx>")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, 'r') as file:
        code = file.read()

    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    executor = Executor(ast)
    executor.execute()

if __name__ == "__main__":
    main()
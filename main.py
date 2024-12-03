from lexer import Lexer
from parser import Parser
from executor import Executor

def main():
    code = """
    x = 5;
    y = x + 3;
    if (y > 5) {
        z = y * 2;
    } else {
        z = y / 2;
    }
    while (x < 10) {
        x = x + 1;
    }
    """
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    print("Tokens:", tokens)

    parser = Parser(tokens)
    ast = parser.parse()
    print("AST:", ast)

    executor = Executor(ast)
    executor.execute()

if __name__ == "__main__":
    main()

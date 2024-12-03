from lexer import Lexer
from parser import Parser
from executor import Executor

def run_program(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    executor = Executor(ast)
    executor.execute()
    
    return executor.variables

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python cli.py <path_to_program>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    variables = run_program(file_path)
    print("Final variable states:", variables)

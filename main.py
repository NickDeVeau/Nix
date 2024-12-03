import sys
import logging
import configparser
from lexer import Lexer
from parser import Parser
from executor import Executor

def create_config():
    config = configparser.ConfigParser()
    config['Logging'] = {
        'level': 'INFO'
    }
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def main():
    # Ensure the config.ini file is created
    create_config()

    if len(sys.argv) != 2:
        print("Usage: python main.py <source_file>.nx")
        sys.exit(1)

    source_file = sys.argv[1]

    if not source_file.endswith('.nx'):
        print("Error: The source file must have a .nx extension")
        sys.exit(1)

    try:
        with open(source_file, 'r') as f:
            code = f.read()
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        # print(f"Tokens: {tokens}")  # Comment out or remove this line
        parser = Parser(tokens)
        ast = parser.parse()
        # print(f"AST: {ast}")  # Comment out or remove this line
        executor = Executor(ast)
        executor.execute()
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()

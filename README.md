# Nix Interpreter

## Overview
The **Nix Interpreter** is a custom-designed programming language interpreter written in Python. It supports essential programming constructs such as variables, arithmetic operations, conditionals, loops, and user-defined functions. The interpreter processes and executes Nix programs using a combination of a lexer, parser, and executor.

## Features
- **Variables and Arithmetic Operations**:  
  Supports variable declarations, assignments, and arithmetic computations.
  
- **Conditionals**:  
  Implements `if-else` statements for conditional logic.
  
- **Loops**:  
  Supports `while` loops for iterative execution.
  
- **Functions**:  
  Allows user-defined functions with parameters and return values.
  
- **Print Statements**:  
  Includes `print` statements for outputting data to the console.

## Installation
To install the Nix interpreter, clone the repository and use `setup.py` to install the package:

```bash
git clone https://github.com/your-username/nix-interpreter.git
cd nix-interpreter
python setup.py install
```

## Usage
Run a Nix script by using the `nix` command followed by the script file path:

```bash
nix example.nx
```

### Example
Create a file named `example.nx` with the following content:

```nix
x = 10;
y = 20;

if (x < y) {
    print("x is less than y");
} else {
    print("x is greater than or equal to y");
}

def add(a, b) {
    return a + b;
}

z = add(x, y);
print("Sum:", z);
```

Run the script:

```bash
nix example.nx
```

## Contribution
Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes.
4. Commit your changes:
   ```bash
   git commit -am "Add new feature"
   ```
5. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
6. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
class Executor:
    def __init__(self, ast):
        self.ast = ast
        self.variables = {}
        self.functions = {}

    def execute(self):
        self.execute_statements(self.ast)

    def execute_statements(self, statements):
        for statement in statements:
            result = self.execute_statement(statement)
            if result is not None:
                return result

    def execute_statement(self, statement):
        kind = statement[0]
        if kind == 'assign':
            self.execute_assignment(statement)
        elif kind == 'if':
            result = self.execute_if(statement)
            if result is not None:
                return result
        elif kind == 'while':
            result = self.execute_while(statement)
            if result is not None:
                return result
        elif kind == 'function':
            self.execute_function_declaration(statement)
        elif kind == 'call':
            return self.execute_function_call(statement)
        elif kind == 'print':
            self.execute_print(statement)
        elif kind == 'return':
            return self.evaluate_expression(statement[1])
        else:
            raise RuntimeError(f"Unknown statement type: {kind}")

    def execute_assignment(self, statement):
        _, identifier, value = statement
        self.variables[identifier] = self.evaluate_expression(value)

    def execute_if(self, statement):
        _, condition, then_branch, else_branch = statement
        if self.evaluate_expression(condition):
            result = self.execute_statements(then_branch)
            if result is not None:
                return result
        elif else_branch:
            result = self.execute_statements(else_branch)
            if result is not None:
                return result

    def execute_while(self, statement):
        _, condition, body = statement
        while self.evaluate_expression(condition):
            result = self.execute_statements(body)
            if result is not None:
                return result

    def execute_function_declaration(self, statement):
        _, name, parameters, body = statement
        self.functions[name] = (parameters, body)

    def execute_function_call(self, expression):
        _, name, arguments = expression
        if name not in self.functions:
            raise RuntimeError(f"Undefined function: {name}")
        parameters, body = self.functions[name]
        if len(arguments) != len(parameters):
            raise RuntimeError(f"Argument count mismatch for function: {name}")
        old_variables = self.variables.copy()
        self.variables = old_variables.copy()
        for param, arg in zip(parameters, arguments):
            self.variables[param] = self.evaluate_expression(arg)
        result = self.execute_statements(body)
        self.variables = old_variables
        return result

    def execute_print(self, statement):
        _, expr = statement
        value = self.evaluate_expression(expr)
        print(value)

    def evaluate_expression(self, expression):
        kind = expression[0]
        if kind == 'number':
            return int(expression[1])
        elif kind == 'string':
            return expression[1][1:-1]
        elif kind == 'identifier':
            if expression[1] in self.variables:
                return self.variables[expression[1]]
            else:
                raise RuntimeError(f"Undefined variable: {expression[1]}")
        elif kind == 'binary':
            operator = expression[1]
            left = self.evaluate_expression(expression[2])
            right = self.evaluate_expression(expression[3])
            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            elif operator == '*':
                return left * right
            elif operator == '/':
                return left / right
            elif operator == '>':
                return left > right
            elif operator == '<':
                return left < right
            elif operator == '==':
                return left == right
            elif operator == '!=':
                return left != right
            elif operator == '>=':
                return left >= right
            elif operator == '<=':
                return left <= right
            else:
                raise RuntimeError(f"Unknown operator: {operator}")
        elif kind == 'unary':
            operator = expression[1]
            operand = self.evaluate_expression(expression[2])
            if operator == '-':
                return -operand
            else:
                raise RuntimeError(f"Unknown unary operator: {operator}")
        elif kind == 'call':
            return self.execute_function_call(expression)
        else:
            raise RuntimeError(f"Unknown expression type: {kind}")

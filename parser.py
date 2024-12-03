class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def parse(self):
        return self.program()

    def program(self):
        statements = []
        while self.position < len(self.tokens) and not self.match('RBRACE'):
            statements.append(self.statement())
        return statements

    def statement(self):
        if self.match('IF'):
            return self.if_statement()
        elif self.match('WHILE'):
            return self.while_statement()
        elif self.match('IDENTIFIER'):
            # Distinguish function calls from assignments
            if self.position + 1 < len(self.tokens) and self.tokens[self.position + 1][0] == 'LPAREN':
                return self.function_call()
            else:
                return self.assignment()
        elif self.match('DEF'):
            return self.function_declaration()
        elif self.match('RETURN'):
            self.consume('RETURN')
            value = self.expression()
            self.consume('SEMICOLON')
            return ('return', value)
        else:
            token = self.tokens[self.position] if self.position < len(self.tokens) else ('EOF', 'end of file')
            raise SyntaxError(f"Unknown statement starting with {token[0]} ('{token[1]}')")

    def if_statement(self):
        self.consume('IF')
        self.consume('LPAREN')
        condition = self.expression()
        self.consume('RPAREN')
        self.consume('LBRACE')
        then_branch = self.program()
        self.consume('RBRACE')
        else_branch = None
        if self.match('ELSE'):
            self.consume('ELSE')
            self.consume('LBRACE')
            else_branch = self.program()
            self.consume('RBRACE')
        return ('if', condition, then_branch, else_branch)

    def while_statement(self):
        self.consume('WHILE')
        self.consume('LPAREN')
        condition = self.expression()
        self.consume('RPAREN')
        self.consume('LBRACE')
        body = self.program()
        self.consume('RBRACE')
        return ('while', condition, body)

    def assignment(self):
        identifier = self.consume('IDENTIFIER')
        self.consume('ASSIGN')
        value = self.expression()
        self.consume('SEMICOLON')
        return ('assign', identifier, value)

    def function_declaration(self):
        self.consume('DEF')
        name = self.consume('IDENTIFIER')
        self.consume('LPAREN')
        parameters = []
        if not self.match('RPAREN'):
            parameters.append(self.consume('IDENTIFIER'))
            while self.match('COMMA'):
                self.consume('COMMA')
                parameters.append(self.consume('IDENTIFIER'))
        self.consume('RPAREN')
        self.consume('LBRACE')
        body = self.program()
        self.consume('RBRACE')
        return ('function', name, parameters, body)

    def function_call(self):
        name = self.consume('IDENTIFIER')
        self.consume('LPAREN')
        arguments = []
        if not self.match('RPAREN'):
            arguments.append(self.expression())
            while self.match('COMMA'):
                self.consume('COMMA')
                arguments.append(self.expression())
        self.consume('RPAREN')
        self.consume('SEMICOLON')
        return ('call', name, arguments)

    def expression(self):
        return self.comparison()

    def comparison(self):
        left = self.addition()
        while self.match('OP') and self.tokens[self.position][1] in ('<', '>', '==', '!=', '<=', '>='):
            operator = self.consume('OP')
            right = self.addition()
            left = ('binary', operator, left, right)
        return left

    def addition(self):
        left = self.multiplication()
        while self.match('OP') and self.tokens[self.position][1] in ('+', '-'):
            operator = self.consume('OP')
            right = self.multiplication()
            left = ('binary', operator, left, right)
        return left

    def multiplication(self):
        left = self.primary()
        while self.match('OP') and self.tokens[self.position][1] in ('*', '/'):
            operator = self.consume('OP')
            right = self.primary()
            left = ('binary', operator, left, right)
        return left

    def primary(self):
        if self.match('NUMBER'):
            return ('number', self.consume('NUMBER'))
        elif self.match('IDENTIFIER'):
            identifier = self.consume('IDENTIFIER')
            if self.match('LPAREN'):
                # Function call within an expression
                self.consume('LPAREN')
                arguments = []
                if not self.match('RPAREN'):
                    arguments.append(self.expression())
                    while self.match('COMMA'):
                        self.consume('COMMA')
                        arguments.append(self.expression())
                self.consume('RPAREN')
                return ('call', identifier, arguments)
            else:
                return ('identifier', identifier)
        elif self.match('LPAREN'):
            self.consume('LPAREN')
            expr = self.expression()
            if not self.match('RPAREN'):
                raise SyntaxError(f"Expected ')', but found {self.tokens[self.position][0]} ('{self.tokens[self.position][1]}')")
            self.consume('RPAREN')
            return expr
        else:
            token = self.tokens[self.position] if self.position < len(self.tokens) else ('EOF', 'end of file')
            raise SyntaxError(f"Expected number, identifier, or '(', but found {token[0]} ('{token[1]}')")


    def match(self, kind):
        if self.position < len(self.tokens) and self.tokens[self.position][0] == kind:
            return True
        return False

    def consume(self, kind):
        if self.match(kind):
            token = self.tokens[self.position]
            self.position += 1
            return token[1]
        else:
            token = self.tokens[self.position] if self.position < len(self.tokens) else ('EOF', 'end of file')
            raise SyntaxError(f"Expected {kind}, but found {token[0]} ('{token[1]}') at position {self.position}")

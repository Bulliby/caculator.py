# **************************************************************************** #
#                                                                              #
#                                                                              #
#    Parser.py                                                                 #
#                                                         ________             #
#    By: bulliby <wellsguillaume+at+gmail.com>           /   ____/_  _  __     #
#                                                       /    \  _\ \/ \/ /     #
#    Created: 2019/03/02 20:02:11 by bulliby            \     \_\ \     /      #
#    Updated: 2019/03/02 20:20:27 by bulliby             \________/\/\_/       #
#                                                                              #
# **************************************************************************** #

#Binary Operator e.g : 12 + 3
class BinOp():
    def __init__(self, left, right, operator):
        self.left = left
        self.right = right
        self.operator = operator

    def __str__(self):
        return "Opérateur binaire {operator} avec left : {left} et right : {right}".format(operator=self.operator, left=self.left, right=self.right)

class Int():
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Interger who's value is {value}".format(value=self.value)

class Parser():
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def __str__(self):
        return 'This object handle the parsing of the expression'

    def getToken(self):
        return self.tokens[self.pos]

    def getNextToken(self):
        self.pos+=1

    def eat(self, token, value):
        """ 
        The eat function permit to check that the token from the Lexer
        follow the given grammar
        """
        if token.token != value:
            raise Exception("Parse Error")
        self.getNextToken()

    def expr(self):
        """
        expr    : term ((PLUS | MINUS) * term)
        """
        node = self.term()
        while self.getToken().token in ['PLUS', 'MINUS']:
            token = self.getToken().token 
            if self.getToken().token == 'PLUS':
                self.eat(self.getToken(), 'PLUS')
            elif self.getToken().token == 'MINUS':
                self.eat(self.getToken(), 'MINUS')
            node = BinOp(node, self.term(), token)
        return node


    def term(self):
        """
        term    : factor ((MUL | DIV) * factor)
        """
        node = self.factor()
        while self.getToken().token in ['MUL', 'DIV']:
            token = self.getToken().token
            if self.getToken().token == 'MUL':
                self.eat(self.getToken(), 'MUL')
            elif self.getToken().token == 'DIV':
                self.eat(self.getToken(), 'DIV')
            node = BinOp(node, self.factor(), token)
        return node

    def factor(self):
        """
        factor  : INTEGER
        """
        integer = self.getToken().value
        self.eat(self.getToken(), 'INT')
        return Int(int(integer))

    def parse(self):
        return self.expr()

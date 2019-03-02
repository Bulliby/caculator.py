# **************************************************************************** #
#                                                                              #
#                                                                              #
#    calculator.py                                                             #
#                                                         ________             #
#    By: bulliby <wellsguillaume+at+gmail.com>           /   ____/_  _  __     #
#                                                       /    \  _\ \/ \/ /     #
#    Created: 2019/03/02 19:55:47 by bulliby            \     \_\ \     /      #
#    Updated: 2019/03/02 19:55:48 by bulliby             \________/\/\_/       #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/python

from Interpreter import Interpreter
from Lexer import Lexer
from Parser import Parser

input = input()

#Lexer
"""
Split user Input in a tab of Tokens
"""
lexer = Lexer(input)
tokens = lexer.splitInput()

#Parser
"""
Use the tokens for build an AST (Abstract Syntax Tree) with the help 
of a Grammar see grammar file.
"""
parser = Parser(tokens)
nodes = parser.parse()

#Interpreter
"""
Go through the AST's nodes in a post order traversal and caluclate
the result.
"""
interpreter = Interpreter(nodes)
integer = interpreter.visitNode(nodes)

print(integer)

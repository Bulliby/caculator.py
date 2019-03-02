# **************************************************************************** #
#                                                                              #
#                                                                              #
#    Interpreter.py                                                            #
#                                                         ________             #
#    By: bulliby <wellsguillaume+at+gmail.com>           /   ____/_  _  __     #
#                                                       /    \  _\ \/ \/ /     #
#    Created: 2019/03/02 19:56:05 by bulliby            \     \_\ \     /      #
#    Updated: 2019/03/02 20:32:40 by bulliby             \________/\/\_/       #
#                                                                              #
# **************************************************************************** #

from Parser import Int

class Interpreter():

    def __init__(self, root):
        self.root = root
        self.total = 0

    def visitNode(self, node):
        if type(node) is not Int:
            left = self.visitNode(node.left)
            right = self.visitNode(node.right)
            result = self.calc(left, right, node)
            return result

        else:
            return node.value

    def calc(self, left, right, node):
        if node.operator == 'PLUS':
            return left + right
        if node.operator == 'MINUS':
            return left - right
        if node.operator == 'DIV':
            return left / right
        if node.operator == 'MUL':
            return left * right

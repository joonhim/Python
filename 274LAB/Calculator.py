import numpy as np
import ArrayStack
import BinaryTree
import ChainedHashTable
import DLList
import operator

class Calculator:
    def __init__(self) :
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k : str, v : float) :
        self.dict.add(k,v)
        
    def matched_expression(self, s : str) -> bool :
        stack = ArrayStack.ArrayStack()
        i = 0
        while i < len(s):
            symbol = s[i]
            if symbol == "(":
                stack.push(symbol)# value []
            elif symbol == ")":
                if len(stack) == 0:
                    return False
                stack.pop()
            i = i + 1
        if len(stack) == 0:
            return True
        else:
            return False



    def build_parse_tree(self, exp : str) ->str:
        if not self.matched_expression(exp):
           return None
        t = BinaryTree.BinaryTree()
        t.r = t.Node("")
        u = t.r
        operators = ["+", "-", "*", "/"]
        for i in exp:
            if i.isalpha() and self.dict.find(i) is None:
                return 0
            elif i == '(':
                # u.add(u.left), u == u.left
                u = u.insert_left()
            elif i in operators:
                u.x = i#u.set_val(i)
                # u.add(u.right), u == u.right
                u = u.insert_right()
            elif i == ')':
                if u.parent is not None:
                    u = u.parent
            elif i.isalpha():#else: # i not in operators:
                u.x = i
                #u.set_val(i)
                u = u.parent
        return t

    def _evaluate(self, root):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        left = root.left
        right = root.right
        if left != None and right != None:
            z = op[root.x]
            return z(float(self._evaluate(left)), float((self._evaluate(right))))
        elif left is None and right is None:
            t = self.dict.find(root.x)
            if t != None: return t
            return root.x
        else:
            if left is not None:
                return self._evaluate(left)
            else:
                return self._evaluate(right)

    def evaluate(self, exp):
        parseTree = self.build_parse_tree(exp)
        if not parseTree:
            return 0
        if parseTree == 0:
            return 0
        else:
            return self._evaluate(parseTree.r)
# class main():
#     PT = Calculator()
#     x = "((a*b)+(c*d))"
#     tree = PT.build_parse_tree(x)
#     PT.set_variable("a", "1.3")
#     PT.set_variable("b", "2.1")
#     PT.set_variable("c", "2.2")
#     PT.set_variable("d", "3")
#     root = round(PT.evaluate(x), 2)
#     print(root)
#
# if __name__ == "__main__":
#
#     main()
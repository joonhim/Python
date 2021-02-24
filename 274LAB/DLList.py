from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self) :
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0
   
    def get_node(self, i : int) -> Node:
        if i < 0 or i > self.n: raise IndexError()
        if i < self.size() / 2:
            node = self.dummy.next
            for j in range(i):
                node = node.next
        else:
            node = self.dummy
            for j in range(self.size() - i):
                node = node.prev
        return node

    def get(self, i) -> np.object:
       return self.get_node(i).x

    def set(self, i : int, x : np.object) -> np.object:
       u = self.get_node(i)
       y = u.x
       u.x = self.x
       return y

    def add_before(self, w : Node, x : np.object) -> Node:
       u = DLList.Node(x)
       u.prev = w.prev
       u.next = w
       u.next.prev = u
       u.prev.next = u
       self.n = self.n+1
       return u

    def add(self, i : int, x : np.object)  :
        if i < 0 or i > self.n: raise IndexError()
        self.add_before(self.get_node(i), x)

    def _remove(self, w : Node) :
       node = w
       node.prev.next = node.next
       node.next.prev = node.prev
       self.n = self.n - 1
       return node.x

    def remove(self, i :int) :
        if i < 0 or i > self.n: raise IndexError()
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x : np.object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        x = True
        #y = 0 #number of iteration
        u = self.dummy.next
        w = self.dummy.prev
        while x == True :
            #if y < self.n / 2:
            if u.x != w.x:
                x = False
                return x
            else:
                return x
            u = u.next
            w = w.prev
            y += 1 #increase the number of iteration processed



    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"


    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x
def main():
    dlist = DLList()
    dlist.add(0, 4)
    dlist.add(0, 1)
    dlist.add(1, 3)
    dlist.add(1, 2)
    dlist.add(4, 5)
    print(dlist)
    print("getting element 1: -> ", dlist.get(0))
    print("removing element at index 2: ->", dlist.remove(2)) # should be 3
    print("removing element at index 3: ->", dlist.remove(3))  # should be 5
if __name__ == "__main__":
    main()
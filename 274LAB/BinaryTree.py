import ArrayQueue
from drawtree import draw_bst

class BinaryTree:
    class Node:
        def __init__(self, x : object, v = None) :
            self.parent = self.left = self.right = None
            self.x = x
            self.v = v

        def set_val(self, x) :
            self.x = x

        def insert_left(self) :
            self.left = BinaryTree.Node('') 
            self.left.parent = self
            return self.left

        def insert_right(self) :
            self.right = BinaryTree.Node('')
            self.right.parent = self
            return self.right

    def __init__(self) : 
        self.r = None
        self.nil = None

    def depth(self, u : Node) -> int:
        if u == self.nil:
            return -1
        d = 0
        while (u != self.r):
            u = u.parent
            d = d+1
        return d

    def size(self) -> int:
        return self._size(self.r)
    
    def _size(self, u : Node) -> int:
        if u == self.nil:
            return 0
        return 1 + self.size(u.left) + self.size(u.right)

    
    def size2(self) -> int:
        u = self.r
        prv = self.nil
        self.n = 0
        while u != self.nil:
            if prv == u.parent:
                self.n = self.n + 1
                if u.left != self.nil:
                    nxt = u.left
                elif u.right != self.nil: nxt = u.right
                else: nxt = u.parent
            elif prv == u.left:
                if u.right != self.nil:
                    nxt = u.right
                else:
                    nxt = u.parent
            else:
                nxt = u.parent
            prv = u
            u = nxt
        return self.n


    def height(self) -> int:
        return self._height(self.r)
    
    def _height(self, u : Node) -> int:
        if u == self.nill:
            return 0
        rh = self._height(u.right)
        lh = self._height(u.left)
        return max(rh, lh) + 1
        #max height of right subtree and left subtree

    
    def traverse(self, u : Node):
        if u == self.nil:
            return
        self.traverse(u.left)
        self.traverse(u.right)


    def traverse2(self):
        u = self.r
        prv = self.nil
        n = 0
        while u != self.nil:
            if prv == u.parent:
                n = n - 1
                #visit u for first time
                if u.left != self.nil: nxt = u.left
                elif u.right != self.nil: nxt = u.left
                else: nxt = u.parent
            else: nxt = u.parent
            prv = u
            u = nxt

    def bf_traverse(self):
        q = ArrayQueue.ArrayQueue()
        l = list()
        if self.r != self.nil:
            q.add(self.r)
            l.append(self.r.v)
        while q.size() > 0:
            u = q.remove()
            if u.left != self.nil:
                q.add(u.left)
                l.append(u.left.v)
            if u.right != self.nil:
                q.add(u.right)
                l.append(u.right.v)
        return l

    def first_node(self):
        w = self.r
        if w == self.nil: return self.nil
        while w.left != self.nil:
            w = w.left
        return w
    
    def next_node(self, w):
        if w.right != self.nil:
            w = w.right
            while w.left != self.nil:
                w = w.left
        else:
            while w.parent != self.nil and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w

    def pre_order(self, u: Node, l:list):
        l.append(u)
        if u.left != self.nil: self.pre_order(u.left, l)
        if u.right != self.nil: self.pre_order(u.right, l)

    def in_order(self, u : Node, l : list) :
        l.append(u.x)#Visit u
        if u.left != self.nil:  self.in_order(u.left, l)
        if u.right != self.nil: self.in_order(u.right, l)

    def post_order(self, u: Node, l:list):
        if u.left != self.nil: self.post_order(u.left, l)
        if u.right != self.nil: self.post_order(u.right, l)
        l.append(u)

    def __str__(self):
        l = []
        self.in_order(self.r, l)
        return ', '.join(map(str, l))
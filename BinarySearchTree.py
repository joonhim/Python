from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self, nil=None):
        BinaryTree.__init__(self)
        self.n = 0
        self.nil = nil
        
    def clear(self):
        self.r = self.nil
        self.n = 0

    def new_node(self, x):
        u = BinaryTree.Node(x)
        u.left = u.right = u.parent = self.nil
        return u
    
        
    def find_last(self, x : object) -> BinaryTree.Node:
        w = self.r
        prev = self.nil
        while w != self.nil:
            prev = w
            if (x < w.x):
                w = w.left
            elif (x > w.x):
                w = w.right
            else:
                return w
        return prev

    def add_child(self, p : BinaryTree.Node, u : BinaryTree.Node) -> bool:
       if p == self.nil:
           self.r = u #inserting into empty tree
       else:
            if u.x < p.x:
               p.left = u
            elif u.x > p.x:
               p.right = u
            else:
                return False
          # u.x == p.x: u.parent == p
            u.parent = p
       self.n += 1
       return True


    def find_eq(self, x : object) -> object:
        u = self.r
        while u != self.nil:
            if x < u.x:
               u = u.left
            elif x > u.x:
               u = u.right
            else:
               return u
        return self.nil

    
    def find(self, x: object) -> object:
        w = self.r
        z = self.nil
        while w != self.nil:
            if x < w.x:
               z = w
               w = w.left
            elif x > w.x:
               w = w.right
            else:
               return w.x
            if z == self.nil: return self.nil
            return z.x

        
    def add(self, key : object, value : object) -> bool:
        p = self.find_last(key)
        return self.add_child(p, BinaryTree.Node(key, value))
        
    def add_node(self, u : BinaryTree.Node) -> bool:
        p = self.find_last(u.x)
        return self.add_child(p, u)
    
    def splice(self, u: BinaryTree.Node):
        if u.left != self.nil and u.right != self.nil: #Exception
            s = u.left
        else:
            s = u.right
        if u == self.r:
            self.r = s
            p = self.nil
        else:
            p = u.parent
            if p.left == u:
                p.left = s
            else:
                p.right = s
        if s != self.nil:
            s.parent = p
        self.n = self.n - 1


    def remove_node(self, u : BinaryTree.Node):
        if u.left == self.nil or u.right == self.nil:
            self.splice(u)
        else:
            w = u.right
            while w.left != self.nil:
                w = w.left
            u.x = w.x
            self.splice(w)

    def remove(self, x : object) -> bool:
        w = self.find_eq(x)
        if w != self.nil:
            self.remove_node(w)
            return True
        else:
            return False


             
    def __iter__(self):
        u = self.first_node()
        while u != self.nil:
            yield u.x
            u = self.next_node(u)

class main():
    BST = BinarySearchTree()
    BST.add(3, "bob")
    BST.add(5, "still")
    BST.add(2, "pees")
    BST.remove(3)
    print(BST)
if __name__ == "__main__":

    main()


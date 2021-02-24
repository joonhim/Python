import Calculator
import BookStore
import BinaryTree
import BinarySearchTree

def menu_calculator() :
    calculator =  Calculator.Calculator()
    option=""
    while option != '0':
        print ("""
        1 Check mathematical expression 
        2 Set Variables
        3 Print In Order
        4 Print Post order
        5 Print Pre Order
        6 Print bf_Traversal
        7 Print Height of Tree
        0 Return to main menu
        
        """)
        option=input()
        if option=="1":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression) :
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is invalid expression")
        if option == "2":
            variable = input("set varialbe: ")
            value = int(input("set value: "))
            calculator.set_variables(variable, value)
        if option == "3":
            tree = BinaryTree.BinaryTree()
            print(tree.in_order())
        if option == '4':
            tree = BinaryTree.BinaryTree()
            print(tree.post_order())
        if option == '5':
            tree = BinaryTree.BinaryTree()
            print(tree.pre_order())
        if option == '6':
            tree = BinaryTree.BinaryTree()
            print(tree.bf_traverse())
        if option == '7':
            tree = BinaryTree.BinaryTree()
            print(tree._height())






        ''' 
        Add the menu options when needed
        '''

def menu_bookstore_system() :
    bookStore = BookStore.BookStore()
    option=""
    while option != '0':
        print("""
        s FIFO shopping cart
        r Max shopping cart
        1 Load book catalog
        2 Remove a book by index from catalog
        3 Add a book by index to shopping cart
        4 Remove from the shopping cart
        5 Search book by infix
        6 Search book by prefix
        7 Search by Best Seller Prefix
        8 Binary Search by Prefix
        9 BFS
        10 DFS
        0 Return to main menu
        """)
        option=input() 
        if option=="r":
            bookStore.setMaxShoppingCart()
        elif option=="s":
            bookStore.setShoppingCart()
        elif option=="1":
            file_name = input("Introduce the name of the file: ")
            bookStore.loadCatalog(file_name) 
            #bookStore.pathLength(0, 159811)
        elif option=="2":
            i = int(("Introduce the index to remove from catalog: "))
            bookStore.removeFromCatalog(i)
        elif option=="3":
            i = int(input("Introduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)
        elif option=="4":
            bookStore.removeFromShoppingCart()
        elif option=="5":
            infix = input("Introduce the query to search: ")
            bookStore.searchBookByInfix(infix)
        elif option=="6":
            prefix = input("Introduce the query to search: ")
            bookStore.searchBookByPrefix(prefix)
        elif option=="7":
            prefix = input("Introduce the query to search: ")
            k = int(input("Up to What number? Enter K: "))
            bookStore.bestSellerPrefix(prefix, k)
        elif option == "8":
            prefix = input("Introduce the query to binary search: ")
            bookStore.binarySearchbyPrefix(prefix)
        elif option == "9":
            r = int(input("Enter Index: "))
            m = int(input("Enter distance from Index: "))
            t = bookStore.similarGraph.bfs2(r,m)
            for i in range(1, len(t)):
                print(bookStore.bookCatalog.get(t[i]))
        elif option == "10":
            r1 = int(input("Enter Index: "))
            r2 = int(input("Enter Distance/Destination: "))
            answer =bookStore.similarGraph.dfs2(r1, r2)
            print("The Separation Deg: ", answer)

        ''' 
        Add the menu options when needed
        '''

#main: Create the main menu
def main() :
    option=""
    while option != '0':
        print ("""
        1 Calculator
        2 Bookstore System
        0 Exit/Quit
        """)
        option=input() 
        
        if option=="1":
            menu_calculator()
        elif option=="2":
            menu_bookstore_system()    

if __name__ == "__main__":
  main()

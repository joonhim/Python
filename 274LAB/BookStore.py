import Book
import SortableBook
import ArrayList
import ArrayQueue
import RandomQueue
import DLList
import SLLQueue
import MaxQueue
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
import AdjacencyList
import time
import algorithms
import AdjacencyMatrix

class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''

    def __init__(self):
        self.shoppingCart = ArrayQueue.ArrayQueue()
        self.indexTitle = BinarySearchTree.BinarySearchTree()
        self.indexSortedTitle = BinarySearchTree.BinarySearchTree()
        self.searchBookByBestSeller = BinaryHeap.BinaryHeap()
        self.dup = BinarySearchTree.BinarySearchTree()
        self.bestSeller = BinaryHeap.BinaryHeap()
        self.loadCatalog("books.txt")
        self.titleCatalog = ArrayList.ArrayList()
        self.bookSortedCatalog = ArrayList.ArrayList()
        self.indexKeys = None #ChainedHashTable.ChainedHashTable()
        self.similarGraph = None #AdjacencyList.AdjacencyList(self.bookCatalog.size())

    def loadCatalog(self, fileName: str):
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = DLList.DLList()
        self.bookSortedCatalog = ArrayList.ArrayList()
        self.indexKeys = ChainedHashTable.ChainedHashTable()

        with open(fileName, encoding='UTF8') as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            # for line in f:
            #     (key, title, group, rank, similar) = line.split("^")
            #     s = Book.Book(key, title, group, rank, similar)
            #     s_s = SortableBook.SortableBook(key, title, group, rank, similar)
            #     d = s
            #     d.rank = d.rank * -1
            #     self.bookSortedCatalog.append(s_s)
            #     self.indexSortedTitle.add(s.title, s)
            #     self.indexTitle.add(s.title, s)
            i = 0
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key,title,group,rank,similar)
                self.bookCatalog.append(s)
                self.indexKeys.add(s.key, i)
                i = i + 1
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")
        self.similarGraph = AdjacencyList.AdjacencyList(self.bookCatalog.size())
        with open(fileName, encoding='UTF8') as f:
            start_time = time.time()
            i = 0
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                l = similar.split()
                for k in range(1, len(l)):
                    j = self.indexKeys.find(l[k])
                    if j != None:
                        self.similarGraph.add_edge(i, j)
                i = i + 1
            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")
           # print(self.bookSortedCatalog.size())

    def binarySearchbyPrefix(self, prefix: str):
        start_time = time.time()
        titleCatalog = ArrayList.ArrayList()
        found = False
        title = SortableBook.SortableBook(0, prefix, " ", 0, None)
        algorithms.merge_sort(self.bookSortedCatalog)
        for book in self.bookSortedCatalog:
            titleCatalog.append(book.title)
        sort_op = input('''
                        Choose one option:

                        1 MergeSort
                        2 QuickSort
                    ''')
        if sort_op == "1":
            algorithms.merge_sort(self.bookSortedCatalog)
            algorithms.merge_sort(titleCatalog)

        elif sort_op == "2":
            algorithms.quick_sort(self.bookSortedCatalog)
            algorithms.quick_sort(titleCatalog)
        if prefix == '':
            print("No Prefix or Title")
        else:
             for x in titleCatalog:
                 if x.startswith(prefix):
                    index = algorithms.binary_search(titleCatalog, x)
                    print(index)
        found = True
        if found:
            pass
        else:
            print('None')
        titleCatalog = None
        elapsed_time = time.time() - start_time
        print(f"Completed in {elapsed_time}seconds")

    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = MaxQueue.MaxQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = SLLQueue.SLLQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i: int):
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def bestSellerPrefix(self, infix: str, k: int):
        if self.bookCatalog == None:
            print('Enter Valid file name: ')
        else:
            start_time = time.time()
            c = 0
            h = ChainedHashTable.ChainedHashTable()
            for book in self.bookCatalog:
                x = book.title
                y = book.rank

                if infix in x:
                    book.rank * -1
                    self.bestSeller.add(book.rank)
                    h.add(y, x)
                if infix == "" and c < 50:
                    book.rank * -1
                    self.bestSeller.add(book.rank)
                    h.add(y, x)
                    c += 1
            for book in range(k):
                x = self.bestSeller.remove()
                print(x * -1)
                print(x, h.find(x))
            elapsed_time = time.time() - start_time
            print(f"Completed in {elapsed_time} seconds")

    def searchBookByBestSeller(self, bestSeller: int):
        self.indexSortedTitle.find(bestSeller)
        print(self.indexSortedTitle.find(bestSeller))

    def addBookByTitle(self, title: str):
        if self.indexTitle.find(title) is not None:
            self.ShoppingCart.add(self.indexTitle.find(title))

    def searchBookByPrefix(self, prefix: str):
        self.indexSortedTitle.find(prefix)
        print(self.indexSortedTitle.find(prefix))

    def searchBookByInfix(self, infix: str):
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''
        start_time = time.time()
        print(self.bookCatalog.size())
        for i in range(self.bookCatalog.size()):
            x = self.bookCatalog.get(i)
            if infix in x.title:
                print(i, x.title, x.key)
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shopping cart
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")



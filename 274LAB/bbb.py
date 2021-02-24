def loadCatalog(self, fileName: str):
    self.bookCatalog = DLList.DLList()
    self.indexKeys = ChainedHashTable.ChainedHashTable()
    self.bookSortedCatalog = ArrayList.ArrayList()
    try:
        with open(fileName, encoding='UTF8') as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            i = 0
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                # s_s= SortableBook.SortableBook(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                self.indexKeys.add(key, i)
                # self.bookSortedCatalog.append(s_s)
                # self.indexTitle.add(s.title, s)
                # self.indexSortedTitle.add(s.title, s)
                i += 1
                self.similarGraph = AdjacencyList.AdjacencyList(self.bookCatalog.size())
        with open(fileName, encoding= 'UTF8') as f:
            i = 0
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                l = similar.split()
                for k in range(1, len(l)):
                    j = self.indexKeys.find(l[k])
                    if j is not None:
                        self.similarGraph.add_edge(i, j)
                i += 1
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")
    except:
        print("There is no such file.")
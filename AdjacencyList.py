"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import DLList
import SLLStack


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, object)
        for i in range(self.n):
            self.adj[i] = DLList.DLList()
            
    def add_edge(self, i : int, j : int):
        # todo
        pass

    def remove_edge(self, i : int, j : int):
        # todo
        pass
                
    def has_edge(self, i : int, j: int) ->bool:
        # todo
        pass
        
    def out_edges(self, i) -> List:
        # todo
        pass

    def in_edges(self, i) -> List:
        # todo
        pass
    
    def bfs(self, r : int, dest: int):
        # todo
        pass    

    def dfs(self, r : int, dest: int):
        # todo
        pass    
                    
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s





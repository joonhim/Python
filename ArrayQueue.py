import numpy as np
from Interfaces import Queue


class ArrayQueue(Queue):
    def __init__(self):
        self.n = 0
        self.j = 0
        self.a = self.new_array(1)

    def new_array(self, n: int) -> np.array:
        return np.zeros(n, np.object)

    def resize(self):
        '''
            Resize the array
        '''
        self.b = self.new_array(max(self.a)*2)
        for k in range(self.n): self.b[k] = self.a[k]
        self.a = self.b

        return self


    def add(self, x: np.object):
        '''
            shift all j > i one position to the right
            and add element x in position i
        '''
        if self.n +1 > len(self.a): self.resize()
        self.a[(self.j + self.n) % len(self.a)] = x
        self.n =+1
        return True

    def remove(self) -> np.object:
        '''
            remove the first element in the queue
        '''
        x = self.j
        if 0 >= self.n:raise Exception("Array is empty")
        for x in range(self.n): x = x+1
        self.n = self.n-1
        if len(self.a >= self.n*3): self.resize()
        return x

    def size(self):
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i < self.n - 1:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator += 1
        else:
            raise StopIteration()
        return x
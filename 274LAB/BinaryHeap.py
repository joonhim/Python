import numpy as np
from Interfaces import Queue


def left(i : int):
    return 2*i + 1

def right(i: int):
    return 2*(i+1)

def parent(i : int):
    return (i-1)//2

class BinaryHeap(Queue):
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n: int) ->np.array:
        return np.zeros(n, np.object)

    def resize(self):
        b = self.new_array(max(2*self.n, 1))
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b

    def add(self, x: object):
        if len(self.a) == self.n: self.resize()
        self.a[self.n] = x
        self.n += 1
        self.bubble_up((self.n - 1))
        return True

    def bubble_up(self, i):
        if i < 0 or i >= self.n: raise Exception
        p = parent(i)
        while i >0 and self.a[i] < self.a[p]:
            self.a[i], self.a[p] = self.a[p], self.a[i]
            i = p
            p = parent(i)

    def remove(self):
        if self.n == 0: raise Exception
        x = self.a[0]
        self.a[0] = self.a[self.n - 1]
        self.n -= 1
        self.trickle_down(0)
        if 3*self.n < len(self.a):
            self.resize()
        return x

    def trickle_down(self, i):
        while i >= 0:
            j = -1
            r = right(i)
            if r < self.n and self.a[r] < self.a[i]:
                l = left(i)
                if self.a[l] < self.a[r]:
                    j = l
                else:
                    j = r
            else:
                l = left(i)
                if l < self.n and self.a[l] < self.a[i]:
                    j = l
            if j >= 0:
                self.a[j], self.a[i] = self.a[i], self.a[j]
            i = j

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[i % len(self.a)]
            if i  < self.n-1:
                s += ","
        return s + "]"

# testing
def main():
    heap = BinaryHeap()
    heap.add(2)
    heap.add(1)
    heap.add(5)

    print(heap)

    print('print size [3]: ', heap.size())

    print('print remove [1]', heap.remove())

    heap.add(4)
    heap.add(1)
    heap.add(3)

    print('print size [5]: ', heap.size())

    print()

    print('print remove order', heap.remove())
    print('print remove order', heap.remove())
    print('print remove order', heap.remove())
    print('print remove order', heap.remove())
    print('print remove order', heap.remove())

if __name__ == "__main__":

    x = BinaryHeap()
    x.add(2)
    x.add(1)
    x.add(5)
    print(x)
    print(x.size())
    x.remove()
    x.add(4)
    x.add(1)
    x.add(3)
    print(x)
    print(x.size)
    x.remove()
    x.remove()
    x.remove()
    x.remove()
    x.remove()

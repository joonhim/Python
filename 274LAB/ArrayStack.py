import numpy as np
from Interfaces import Stack


class ArrayStack(Stack):
    '''
        ArrayStack: Implementation of the Stack interface based on Arrays.
        All the @abstractemthods should be implemented.
        An instance of ArrayStack has access to all the methods in ArrayStack and
        all the methods of the base class (Stack). When executing a method, it executes
        the method of ArrayStack, if it does not exists, it executes the method in the
        Base class (Stack).
        For exmaple,
        s = ArrayStack()
        print(s)
        print(len(s))
    '''

    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n: int) -> np.array:
        return np.zeros(n, np.object)

    def resize(self):
        '''
            Resize the array
        '''
        b = self.new_array(max(1,2 * self.n))
        for k in range(self.n):
            b[k]= self.a[k % len(self.a)]
        self.a = b


    def get(self, i: int) -> np.object:
       if i < 0 or i >= self.n : raise IndexError()
       return self.a[i]

    def set(self, i: int, x: np.object) -> np.object:
        if i < 0 or i >= self.n: raise IndexError()
        y = self.a[i]
        self.a[i] = x
        return y

    def add(self, i: int, x: np.object):
        if i < 0 or i > self.n: Exception()
        '''
            shift all j > i one position to the right
            and add element x in position i
        '''
        if self.n == len(self.a):
            self.resize()
        self.a[i+1:self.n] = self.a[i:self.n-1]
        self.a[i] = x
        self.n = self.n + 1


    def remove(self, i: int) -> np.object:
        '''
            remove element i and shift all j > i one
            position to the left
        '''
        if i < 0 or i >= self.n: raise Exception()
        x = self.a[i]
        self.n = self.n - 1
        if len(self.a) >=(self.n*3): self.resize()
        return x


    def push(self, x: np.object):
        self.add(self.n, x)

    def pop(self) -> np.object:
        return self.remove(self.n - 1)

    def size(self):
        '''
            size: Returns the size of the stack
            Return: an integer greater or equal to zero representing the number
                    of elements in the stack
        '''
        return self.n

    def __str__(self) -> str:
        '''
            __str__: Returns the content of the string using print(s)
            where s is an instance of the ArrayStack
            Return: String with the content of the stack
        '''
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[i]
            if i < self.n - 1:
                s += ","
        return s + "]"

    def __iter__(self):
        '''
            Initialize the iterator. It is to be use in for loop
        '''
        self.iterator = 0
        return self

    def __next__(self):
        '''
            Move to the next item. It is to be use in for loop
        '''
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator += 1
        else:
            raise StopIteration()
        return x
#class main:
def main():
    list = ArrayStack()
    list.push(3)
    list.push(7)
    list.push(10)
    list.push(5)
    list.push(2)
    print(list)
    print("Removing -> ", list.pop())
    print(list)
    print("Removing -> ", list.pop())
    print(list)
    print("Removing -> ", list.pop())
    print(list)
    print("Removing -> ", list.pop())
    print(list)
    print("Removing -> ", list.pop())
    print(list)


if __name__ == "__main__":
    main()

        #' Add 5 elements and remove them checking that they are in opposite order of insertion, e.g.,'
       # 'Inserting the sequence 5,4,3,2,1 result in the sequence 1,2,3,4,5 when removing'







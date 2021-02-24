from SLLQueue import SLLQueue
from SLLStack import SLLStack

class MaxQueue(SLLQueue):
    def __init__(self):
        SLLQueue.__init__(self)
        self.deque = self.DLList()
    def add(self, x : object)  :
       super().add(x)
       if self.deque == 0:
          self.deque.add(0,x)
       else:
            while self.deque != 0 and self.deque.tail.x < x:
                self.deque.remove(self.deque.n - 1)
            self.deque.add(self.deque.n, x)

    def remove(self) -> object:
       if self.n == 0:
           return None
       if self.prev.x == self.deque.prev.x:
           self.prev.remove(0)
       return super().remove()


    def max(self) -> object:
        if self.deqeue == 0:
            return None
        return self.deque.prev.x
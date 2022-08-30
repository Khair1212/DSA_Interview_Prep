class Queue:
    def __init__(self, maxSize):
        self.items = maxSize* [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top +1 == self.maxSize:
            return True
        return False

    def is_empty(self):
        if self.top == -1:
            return True
        return False

    def enqueue(self, value):
        if self.isFull():
            return "The Queue is Full"
        else:
            if self.top+1 == self.maxSize: # Top reached end of queue limit
                self.top = 0
            else:
                self.top+=1
                if self.start == -1: # First element getting inserted
                    self.start += 1
            self.items[self.top] = value
            return "The element is inserted"

    def dequeue(self):
        if self.is_empty():
            return "The Queue is empty!"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top: # Last element getting deleted
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize: # if start is the last index then move to 0
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement

    def peek(self):
        if self.is_empty():
            return " The Queue is Empty!"
        return self.items[self.start]

    def delete(self):
        self.items = self.maxSize * [None]
        self.top = - 1
        self.start = -1

q = Queue(4)
print(q.isFull())
print(q.enqueue(1))
print(q.enqueue(2))
print((q.dequeue()))
print(q.peek())


# Implement Queue class which implements a queue using two stacks

class Stack:
    def __init__(self):
        self.stack1 = []

    def __len__(self):
        return len(self.stack1)

    def push(self, value):
        self.stack1.append(value)

    def pop(self):
        if len(self.stack1) == 0:
            return None
        return self.stack1.pop()


class QueueviaStack:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self, value):
        self.inStack.push(value)

    def dequeue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop()

        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return result

q = QueueviaStack()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.enqueue(4))
print(q.dequeue())
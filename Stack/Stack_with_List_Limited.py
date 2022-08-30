class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        return False

    def push(self, value):
        if self.isFull():
            return 'The Stack is Full'
        self.list.append(value)
        return "The element has been succesfully inserted"

    def pop(self):
        if self.isEmpty():
            return "The stack is already empty"
        val = self.list.pop()
        return val

    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list[-1]

    def delete(self):
        self.list = None

s = Stack(5)
print(s.push(1))
print(s.push(2))
print(s.push(3))
print(s.push(4))
print(s.push(5))
print(s.push(6))
print(s.pop())
print(s.peek())


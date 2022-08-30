class Queue:
    def __init__(self):
        self.list = []


    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)


    def isEmpty(self):
        if self.list == []:
            return True
        return False

    def enqueue(self, value):
        self.list.append(value)
        return "The element has been succesfully inserted"

    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty!"
        val = self.list.pop(0)
        return val

    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.list[0]

    def delete(self):
        self.list = None

s = Queue()
print(s.enqueue(1))
print(s.enqueue(2))
print(s.enqueue(3))
print(s.dequeue())
print(s)
print(s.peek())
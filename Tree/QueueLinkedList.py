class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None


    def __str__(self):
        return  str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        return False

    def enqueue(self, value):
        newNode = Node(value)

        if self.linkedList.head is None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
        return "The value is inserted!"

    def dequeue(self):
        if self.isEmpty():
            return "The Queue is Empty!"

        tempNode = self.linkedList.head
        if self.linkedList.head == self.linkedList.tail:
            self.linkedList.head = None
            self.linkedList.tail = None
        else:
            self.linkedList.head = self.linkedList.head.next
        return tempNode

    def peek(self):
        if self.isEmpty():
            return "The Queue is Empty!"
        return self.linkedList.head

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None

# q = Queue()
# print(q.enqueue(1))
# print(q.enqueue(2))
# print(q.enqueue(3))
# print(q.enqueue(5))
# print(q)
# print(q.dequeue())
# print(q)
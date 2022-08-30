class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


class Stack:

    def __init__(self):
        self.LinkedList = LinkedList()

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        return False

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.LinkedList.head
        self.LinkedList.head = newNode
        return "The node is successfully inserted"

    def pop(self):
        if self.isEmpty():
            return "The Stack is Empty!"
        dlt_node = self.LinkedList.head
        self.LinkedList.head = self.LinkedList.head.next
        return dlt_node.value

    def peek(self):
        if self.isEmpty():
            return "The Stack is Empty"
        return self.LinkedList.head.value

    def delete(self):
        self.LinkedList.head = None
        return "The Stack is Deleted"


s = Stack()
print(s.pop())
print(s.push(1))
print(s.push(2))
print(s.push(3))
print(s.push(4))
print(s.pop())
print(s.peek())
print(s.pop())
print(s.peek())
print(s.isEmpty())
print(s.peek())
# how would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should be all operate in O(1)


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


class Stack:

    def __init__(self):
        self.LinkedList = LinkedList()
        self.minNode = None

    def min(self):
        return self.minNode.value if self.minNode else None

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        return False

    def push(self, value):

        newNode = Node(value)
        newNode.next = self.LinkedList.head
        self.LinkedList.head = newNode

        # update minNonde
        if not self.minNode:
            self.minNode = Node(value)
        elif value <= self.minNode.value:
            self.minNode = Node(value, self.minNode.next)


        return "The node is successfully inserted"

    def pop(self):
        if self.isEmpty():
            return "The Stack is Empty!"
        dlt_node = self.LinkedList.head
        self.LinkedList.head = self.LinkedList.head.next

        # update minNode:
        if dlt_node.value == self.minNode.value:
            self.minNode = self.minNode.next
        return dlt_node.value

    def top(self) -> int:
        return self.LinkedList.head.value if self.LinkedList.head else -1

    def peek(self):
        if self.isEmpty():
            return "The Stack is Empty"
        return self.LinkedList.head.value

    def delete(self):
        self.LinkedList.head = None
        return "The Stack is Deleted"

    def display(self) -> None:
        runner = self.LinkedList.head
        while(runner):
            print(f"{runner.value}->", end='')
            runner = runner.next

s = Stack()
print(s.pop())
print(s.push(-2))
print(s.push(0))
print(s.display())
print(s.top())
print(s.push(-3))
print(s.display())
print(s.peek())
print(s.pop())
print(s.display())
print(s.peek())
print(s.min())

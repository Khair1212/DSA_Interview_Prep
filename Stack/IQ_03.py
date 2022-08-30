# You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has the same maximum capacity.
#
# Implement the DinnerPlates class:
#
# DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks capacity.
# void push(int val) Pushes the given integer val into the leftmost stack with a size less than capacity.
# int pop() Returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns -1 if all the stacks are empty.
# int popAtStack(int index) Returns the value at the top of the stack with the given index index and removes it from that stack or returns -1 if the stack with that given index is empty.


class PlateStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return self.stacks

    def push(self, item):
        if len(self.stacks)> 0 and (len(self.stacks[-1])) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        while len(self.stacks) and (len(self.stacks[-1])) == 0:
            self.stacks.pop()

        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()


    def pop_at(self, stackNumber):
        if len(self.stacks[stackNumber]) > 0:
            return self.stacks[stackNumber].pop()
        else:
            return None

s = PlateStack(3)
print(s.push(1))
print(s.push(2))
print(s.push(3))
print(s.push(4))
print(s.pop_at(0))
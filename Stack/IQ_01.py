# use a single list to implement three stacks

class MultiStack:
    def __init__(self, stacksize):
        self.numberstacks = 3
        self.custList = [0] * (stacksize * self.numberstacks) # Stack list
        self.sizes = [0] *  self.numberstacks  # individual stack size
        self.stacksize = stacksize


    def isFull(self, stacknum):
        if (self.sizes[stacknum] == self.stacksize):
            return True
        return False

    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        return False

    def indexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1


    def push(self, value, stacknum):
        if self.isFull(stacknum):
            return "The stack is full"
        else:
            self.sizes[stacknum] += 1
            self.custList[self.indexOfTop(stacknum)] = value


    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return "The stack is empty!"
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            self.custList[self.indexOfTop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value

    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return "The stack is empty!"
        else:
            value  = self.custList[self.indexOfTop(stacknum)]
            return value



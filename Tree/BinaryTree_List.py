class BinaryTree:
    def __init__(self, size):
        self.list = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    # TC : O(1), SC: O(1)
    def insert(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The BT is Full!"
        else:
            self.list[self.lastUsedIndex + 1] = value
            self.lastUsedIndex += 1
            return "The value has been successfully inserted"

    # TC : O(N), SC: O(1)
    def search(self, value):
        for i in range(len(self.list)):
            if self.list[i] == value:
                return "Success"
        return "Not Found"

    # TC : O(N), SC: O(N)
    def preorder(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.list[index])
        self.preorder(index * 2)
        self.preorder(index * 2 + 1)

    # TC : O(N), SC: O(N)
    def inorder(self, index):
        if index > self.lastUsedIndex:
            return
        self.inorder(index * 2)
        print(self.list[index])
        self.inorder(index * 2 + 1)

    # TC : O(N), SC: O(N)
    def postorder(self, index):
        if index > self.lastUsedIndex:
            return
        self.postorder(index * 2)
        self.postorder(index * 2 + 1)
        print(self.list[index])

    # TC : O(N), SC: O(1)
    def levelorder(self, index):
        for i in range(index, self.lastUsedIndex + 1):
            print(self.list[i])
    # TC : O(N), SC: O(1)
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "There's not any node to delete"

        for i in range(1, self.lastUsedIndex + 1):
            if self.list[i] == value:
                self.list[i] = self.list[self.lastUsedIndex]
                self.list[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The Node has been successfully deleted!"

    # TC : O(1), SC: O(1)
    def deleteTree(self, value):
        self.list = None
        return "The BT has been successfully deleted!"


BT = BinaryTree(8)
BT.insert("Drinks")
BT.insert("Hot Drinks")
BT.insert("Cold Drinks")
BT.insert("Tea")
BT.insert("Coffee")

print(BT.search('Hot Drinks'))
# BT.preorder(1)
BT.levelorder(1)
BT.deleteNode("Cold Drinks")
BT.levelorder(1)

import sys

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, 'C:/Users/kawsm/Downloads/DSA_Interview_Problems/DSA_Interview_Prep')

from Queue.QueueLinkedList import Queue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    # T(C): O(logN), S(C): O(logN)
    def insert(self, rootNode, data):
        if rootNode.data == None:
            rootNode.data = data
        elif data <=rootNode.data:
            if rootNode.leftChild is None:
                rootNode.leftChild = BSTNode(data)
            else:
                self.insert(rootNode.leftChild, data)
        else:
            if rootNode.rightChild is None:
                rootNode.rightChild = BSTNode(data)
            else:
                self.insert(rootNode.rightChild, data)

        return "The node has been successfully inserted!"

    # T(C): O(N), S(C): O(N)
    def preorder(self, rootNode):
        if rootNode is None:
            return

        print(rootNode.data)
        self.preorder(rootNode.leftChild)
        self.preorder(rootNode.rightChild)

    # T(C): O(N), S(C): O(N)
    def inorder(self, rootNode):
        if rootNode is None:
            return
        self.inorder(rootNode.leftChild)
        print(rootNode.data)
        self.inorder(rootNode.rightChild)

    # T(C): O(N), S(C): O(N)
    def postorder(self, rootNode):
        if rootNode is None:
            return
        self.postorder(rootNode.leftChild)
        self.postorder(rootNode.rightChild)
        print(rootNode.data)

    # T(C): O(N), S(C): O(N)
    def levelorder(self, rootNode):
        if rootNode is None:
            return
        q = Queue()
        q.enqueue(rootNode)
        while not q.isEmpty():
            node = q.dequeue()
            print(node.value.data)

            if node.value.leftChild is not None:
                q.enqueue(node.value.leftChild)
            if node.value.rightChild is not None:
                q.enqueue(node.value.rightChild)

    # T(C): O(logN), S(C): O(logN)
    def search(self, rootNode, value):
        if rootNode is None:
            return "The BST is empty "

        if rootNode.data == value:
            return "The value is Found"
        elif value < rootNode.data:
            if rootNode.leftChild and value == rootNode.leftChild.data:
                return "The value is found"
            elif rootNode.leftChild:
                self.search(rootNode.leftChild, value)
        else:
            if rootNode.rightChild and value == rootNode.rightChild.data:
                return "The value is found"
            elif rootNode.rightChild:
                self.search(rootNode.rightChild, value)

        return "The value is not found!"

    def minValueNode(self, bstNode):
        current = bstNode
        while current.leftChild is not None:
            current = current.leftChild
        return current


    # Delete has 3 condition:
    #   1) The node to be deleted is a leaf node
    #   2) The node has one child
    #   3) The node has two child
    # T(C): O(logN), S(C): O(logN)
    def delete(self, rootNode, value):
        if rootNode is None:
            return rootNode
        if value < rootNode.data:
            rootNode.leftChild = self.delete(rootNode.leftChild,value)

        elif value > rootNode.data:
            rootNode.rightChild = self.delete(rootNode.rightChild, value)
        else:
            # has no child
            if not rootNode.leftChild and rootNode.rightChild:
                rootNode = None
                return rootNode

            # has 1 children
            elif rootNode.leftChild is None:
                temp = rootNode.rightChild
                rootNode = None
                return temp
            elif rootNode.rightChild is None:
                temp = rootNode.leftChild
                rootNode = None
                return temp
            else:
                # has 2 children
                temp = self.minValueNode(rootNode.rightChild)
                rootNode.data = temp.data
                rootNode.rightChild = self.delete(rootNode.rightChild, temp.data)
        return rootNode


    def deleteBST(self, rootNode):
        rootNode.data = None
        rootNode.leftChild = None
        rootNode.rightChild = None
        return "The BST is successfully deleted!"

newBST = BSTNode(None)
newBST.insert(newBST, 70)
newBST.insert(newBST, 60)
newBST.insert(newBST, 80)
newBST.insert(newBST, 50)
newBST.insert(newBST, 90)

newBST.levelorder(newBST)
# newBST.preorder(newBST)
# newBST.inorder(newBST)
# newBST.postorder(newBST)
print(newBST.search(newBST, 79))
newBST.delete(newBST, 700)
newBST.levelorder(newBST)
print(newBST.deleteBST(newBST))
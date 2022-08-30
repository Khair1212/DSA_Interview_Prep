import QueueLinkedList as queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


    # TC: O(N) , SC: O(N)
    def preorder(self, rootNode):
        if not rootNode:
            return
        print(rootNode.data)

        self.preorder(rootNode.leftChild)
        self.preorder(rootNode.rightChild)

    # Iterative
    # TC : O(N), SC: O(N)
    def preorder_itr(self, rootNode):  # returns list
        stack, res = [rootNode], []

        while stack:
            node = stack.pop()

            if node:
                res.append(node.data)
                stack.append(node.rightChild)  # append right first to get the left one first in Lifo
                stack.append(node.leftChild)
        return res

    # Recursive
    # TC : O(N), SC: O(N)
    def inorder(self, root):
        if root:
            self.inorder(root.leftChild)
            print(root.data)
            self.inorder(root.rightChild)

    # Iterative
    # TC : O(N), SC: O(N)
    def inorder_itr(self, root):
        res, stack = [], []

        # this following "while True" block keeps running until "return"
        while True:
            # goes all the way to left end's None, append every step onto "stack"
            while root:
                stack.append(root)
                root = root.leftChild

            # if stack has nothing left, then return result
            if not stack:
                return res

            # take the last step out, append its value to result
            node = stack.pop()
            res.append(node.data)
            # moves to right before going all the way to left end's None again
            root = node.rightChild

    # recursive
    # TC : O(N), SC: O(N)
    def postorder(self, root):
        if root:
            self.postorder(root.leftChild)
            self.postorder(root.rightChild)
            print(root.data)

    # iterative
    # TC : O(N), SC: O(N)
    def postorder_itr(self, root):
        traversal, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    traversal.append(node.data)
                else:
                    # post-order
                    stack.append((node, True))
                    stack.append((node.rightChild, False))
                    stack.append((node.leftChild, False))

        return traversal

    # Levelorder using Queue (TC: O(N), SC: O(N))
    def levelorder(self, root):
        if not root:
            return
        else:
            q = queue.Queue()
            q.enqueue(root)
            while not q.isEmpty():
                node = q.dequeue()
                print(node.value.data)
                if node.value.leftChild is not None:
                    q.enqueue(node.value.leftChild)
                if node.value.rightChild is not None:
                    q.enqueue(node.value.rightChild)

    # we shall use level order traversal because queue performs better than stack

    # TC : O(N), SC: O(N)
    def search(self, rootNode, val):
        if not rootNode:
            return "The Binary Tree does not exist"
        else:
            q = queue.Queue()
            q.enqueue(rootNode)
            while not q.isEmpty():
                node =  q.dequeue()
                if node.value.data == val:
                    return "Success"

                if node.value.leftChild is not None:
                    q.enqueue(node.value.leftChild)
                if node.value.rightChild is not None:
                    q.enqueue(node.value.rightChild)
            return "Not Found"

    # using level-order
    # TC : O(N), SC: O(N)
    def insert(self, rootNode, val):
        newNode = TreeNode(val)
        if not rootNode:
            rootNode = newNode
        else:
            q = queue.Queue()
            q.enqueue(rootNode)

            while not q.isEmpty():
                node = q.dequeue()

                if node.value.leftChild is not None:
                    q.enqueue(node.value.leftChild)
                else:
                    node.value.leftChild = newNode
                    return "Successfully inserted"
                if node.value.rightChild is not None:
                    q.enqueue(node.value.rightChild)
                else:
                    node.value.rightChild = newNode
                    return "Successfully inserted"

    # TC : O(N), SC: O(N)
    def getDeepestNode(self,rootNode):
        if not rootNode:
            return
        else:
            q = queue.Queue()
            q.enqueue(rootNode)
            while not q.isEmpty():
                node = q.dequeue()

                if node.value.leftChild is not None:
                    q.enqueue(node.value.leftChild)
                if node.value.rightChild is not None:
                    q.enqueue((node.value.rightChild))

            deepestNode = node.value
            return deepestNode
    # TC : O(N), SC: O(N)
    def deleteDeepestNode(self, rootNode, dNode):
        if not rootNode:
            return
        else:
            q = queue.Queue()
            q.enqueue(rootNode)

            while not q.isEmpty():
                node = q.dequeue()
                if node is dNode:
                    node.value = None
                    return

                if node.value.rightChild:
                    if node.value.rightChild is dNode:
                        node.value.rightChild = None
                        return
                    else:
                        q.enqueue((node.value.rightChild))

                if node.value.leftChild:
                    if node.value.leftChild is dNode:
                        node.value.leftChild = None
                        return
                    else:
                        q.enqueue((node.value.leftChild))

    # using the level-order
    # Replace the node with the deepest node, then then delete the deepest node
    # TC : O(N), SC: O(N)
    def delete(self, rootNode, val):
        if not rootNode:
            return "The BT does not exist"
        q = queue.Queue()
        q.enqueue(rootNode)

        while not q.isEmpty():
            node = q.dequeue()
            if node.value.data == val:
                dNode = self.getDeepestNode(rootNode)
                node.value.data = dNode.data
                self.deleteDeepestNode(rootNode, dNode)
                return "Successfully Deleted"

            if node.value.leftChild is not None:
                q.enqueue(node.value.leftChild)
            if node.value.rightChild is not None:
                q.enqueue((node.value.rightChild))
        return "Value not found to delete"


    def deleteTree(self, rootNode):
        rootNode.data = None
        rootNode.leftChild = None
        rootNode.rightChild = None
        return "The BT has been successly Deleted"


newBT = TreeNode("Drinks")
newBT.insert(newBT, "Hot")
newBT.insert(newBT, "Cold")
newBT.insert(newBT, "Hot-Coffee")
newBT.insert(newBT, "Hot Cake")
newBT.insert(newBT, "Cold-Coffee")
newBT.insert(newBT, "Cold-Juice")

print(newBT)

# newBT.preorder(newBT)
# print(newBT.preorder_itr(newBT))

# newBT.inorder(newBT)
# print(newBT.inorder_itr(newBT))

# newBT.postorder(newBT)
# print(newBT.postorder_itr(newBT))

# newBT.levelorder(newBT)
# print(newBT.search(newBT, "Tea"))



dNode = newBT.getDeepestNode(newBT)
newBT.deleteDeepestNode(newBT, dNode)
newBT.levelorder(newBT)
newBT.delete(newBT, "Hot")
newBT.levelorder(newBT)
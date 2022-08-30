# write code to find the intersected node of two linked list

# using extra space
from LinkedList import LinkedList, Node



def getIntersectionNode(headA, headB):

    d = {}

    while headA is not None:
        d[headA] = 1
        headA = headA.next

    while headB is not None:
        if headB in d.keys():
            return headB
        headB = headB.next

# Without extra space

def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False

    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)

    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return shorterNode


# Helper addition method

def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode

    llB.tail.next = tempNode
    llB.tail = tempNode

llA = LinkedList()
llA.generate(3, 0, 10)

llB = LinkedList()
llB.generate(4, 0, 10)

addSameNode(llA, llB, 11)
addSameNode(llA, llB, 13)
print(llA)
print(llB)

print(intersection(llA, llB))
print(getIntersectionNode(llA.head, llB.head))

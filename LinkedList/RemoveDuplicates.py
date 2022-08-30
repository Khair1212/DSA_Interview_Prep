# Write code to remove duplicates from an unsorted linked list

from LinkedList import LinkedList

def removeDuplicates(ll):
    if ll.head is None:
        return
    else:
        currNode = ll.head

    dic = {}
    dic[currNode.value] = 1
    while currNode and currNode.next:
        if currNode.next.value in dic:
            currNode.next = currNode.next.next
        else:
            dic[currNode.next.value] = 1
        currNode = currNode.next

    return ll

ll = LinkedList()
ll.generate(20, 0, 99)
print(ll)
print(removeDuplicates(ll))
# Write a code to partition a linked list around a value x, sucj that all nodes less than x come before all nodes greater than or equal to x

from LinkedList import LinkedList

def partition(head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    pointer1 = None
    current = head
    prev = head
    while current:
        if current.value < x:
            if current == head or prev == pointer1:
                pointer1 = current
                prev = current
                current = current.next

            elif pointer1 is None:
                pointer1 = current
                prev.next = current.next
                pointer1.next = head
                head = pointer1
                current = prev.next
            else:
                prev.next = current.next
                current.next = pointer1.next
                pointer1.next = current
                pointer1 = current
                current = prev.next

        else:
            prev = current
            current = current.next

    return head

ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(ll.head.next.next.value)

head = (partition(ll.head, 44))
while head:
    print(f'{head.value}->', end = "")
    head = head.next

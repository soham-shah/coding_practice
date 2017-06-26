from LinkedList import *

def deleteDups(llist):
    if (llist.head != None):
        current = llist.head
        values =  {current.value: 1}
        while current.next != None:
            if current.next.value in values:
                current.next = current.next.next
            else:
                values[current.next.value] = 1
                current = current.next

# From the github
def deleteDups2(linkedlist):
    currNode = linkedlist.head
    while currNode != None:
        runner = currNode
        while runner.next != None:
            if runner.next.value == currNode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        currNode = currNode.next

L1 = LinkedList([9, 3, 3, 7])
print L1
deleteDups(L1)
print L1
print
L2 = LinkedList([9, 3, 3, 7])
print L2
deleteDups2(L2)
print L2
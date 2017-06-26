from LinkedList import *

# iterative solution
def kth_to_last(linkedlist, k):
	runner = linkedlist.head
	lagging = linkedlist.head

 	diff = 0
	while diff != k:
		runner = runner.next
		diff += 1

	while runner != None:
		runner = runner.next
		lagging = lagging.next

	return lagging.value

# recursive solution
def kth_to_last_recur(linkedlist, k):
	print(linkedlist)
	num = 0
	if linkedlist == None:
		return 0
	else:
		num = kth_to_last_recur(linkedlist.head.next, k)

	if num == k:
		print "The 3th to last element is", linkedlist.head.value
	else:
		return num + 1


# test from CTCi github
L = LinkedList([8, 0, 100])
print L
print "The 3th to last element is", kth_to_last(L, 3)

print kth_to_last_recur(L, 3)
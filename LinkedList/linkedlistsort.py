class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, new_value):
        new_node = Node(new_value)

        #Allocated the new node.
        #if the head is none, make this node the head node
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
    def sortedMerge(self, a, b):
        result = None
        if a == None:
            return b
        if b == None:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next,b)
        else:
            result = b
            result.next = self.sortedMerge(a,b.next)
        return result
    def mergeSort(self, h):
        #h is a linked list
        if h == None or h.next == None:
             return h
        #get the middle of the list
        middle = self.getMiddle(h)
        next_to_middle = middle.next
        #setting the next of middle to none
        middle.next = None
        #performing mergesort on left list
        left = self.mergeSort(h)
        #performing mergeSort on right side
        right = self.mergeSort(next_to_middle)
        sortedlist = self.sortedMerge(left, right)
        return sortedlist
    #Utility function to get the middle
    #of the linked list.
    def getMiddle(self, head):
        if(head == None):
            return head
        slow = head
        fast = head
        while(fast.next != None and fast.next.next!=None):
            fast = fast.next.next
            slow = slow.next
        return slow
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end = " ")
        curr_node = curr_node.next
    print(' ')

li = LinkedList()
li.append(32)
li.append(21)
li.append(20)
li.append(10)
li.append(15)

li.head = li.mergeSort(li.head)
print("Sorted Linkedlist is :")
printList(li.head)


        
        

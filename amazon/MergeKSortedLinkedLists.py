# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class ListNode:
    def __init__(self, val = 0, next  = None):
        self.val = val
        self.next = next
    
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #we need to just insert the nodes in the list into heap 
        # after all the nodes are inserted just remove them 
        #one by one and insert them into the new list
        
        q = []
        c = 0
        for node in lists:
            # lists contain head of each list.
            while node:
                heapq.heappush(q,node.val)
                c+=1
                node = node.next
        head = ListNode()
        temp = head
        for i in range(c):
            node = ListNode(heapq.heappop(q))
            temp.next = node
            temp = temp.next
        return head.next
        



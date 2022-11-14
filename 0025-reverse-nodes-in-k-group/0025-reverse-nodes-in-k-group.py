# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        store = []
        
        temp = head
        
        while temp:
            var = []
            i = 0
            while i < k and temp:
                var.append(temp)
                i += 1
                temp = temp.next
                
            var.reverse()
            store.append(var)
        
        head = temp = ListNode()
        for i in range(len(store)):
            if len(store[i]) == k:
                for j in range(len(store[i])):
                    temp.next = store[i][j]
                    temp = temp.next
            else:
                store[i].reverse()
                for j in range(len(store[i])):
                    temp.next = store[i][j]
                    temp = temp.next
                
        temp.next = None      
        return head.next
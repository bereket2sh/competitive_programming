# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        p1 = head
        p2 = head.next
        p1.next = None
        while p2:
            temp = p1
            p1 = p2
            p2 = p2.next
            p1.next = temp
            
        return p1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def _reverse(node,prev = None):
#             if not node:
#                 return prev
#             temp = node.next
#             node.next = prev

#             return _reverse(temp,node)
        
#         return _reverse(head)
        

    
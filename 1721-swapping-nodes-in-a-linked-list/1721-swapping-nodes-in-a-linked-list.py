# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp, size = head, 0
        while temp:
            size += 1
            temp = temp.next
            
        def find(n):
            temp = head
            while n:
                temp = temp.next
                n -= 1
            return temp
            
            
        first_node, last_node = find(k - 1), find(size - k)        
        first_node.val, last_node.val = last_node.val, first_node.val
        
        return head
            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp, size = head, 0
        while temp:
            size += 1
            temp  = temp.next
            
        prev, cur = head, head.next
        
        for _ in range(size//2):
            prev, cur = prev.next, cur.next
            
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            
        ans = 0
        
        for _ in range(size//2):
            ans = max(ans, head.val + prev.val)
            head , prev = head.next, prev.next
            
        return ans
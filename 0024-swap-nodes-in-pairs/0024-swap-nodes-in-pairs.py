# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while not head or not head.next:
            return head
        
        dummy  = ListNode(0, head)
        temp = dummy
        
        fst , snd, last = head, head.next, head.next.next
        
        while snd:
            temp.next = snd
            snd.next = fst
            fst.next = last
            if not last or not last.next:
                break
            temp, fst, snd, last = fst, last, last.next, last.next.next
            
            
            
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
            
        def buildTree(arr):
            if not arr:
                return None
            
            mid = len(arr) // 2
            
            root = TreeNode(arr[mid])
            
            root.left = buildTree((arr[:mid]))
            root.right = buildTree(arr[mid + 1: ])
            
            return root
        
        return buildTree(arr)
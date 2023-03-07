# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return None
        self.ans = None
        
        def helper(node):
            if not node:
                return 
            
            if node.val == val:
                self.ans =  node
            
            helper(node.left)
            helper(node.right)
            
        helper(root)
        return self.ans
    
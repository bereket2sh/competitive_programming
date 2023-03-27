# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.ans = float('inf')
        self.prev = None
        
        def dfs(node):
            
            if not node:
                return
            
            dfs(node.left)
            
            if self.prev:
                self.ans = min(self.ans, node.val - self.prev.val )
                
            self.prev = node
            dfs(node.right)
            
        
        dfs(root)
        
        return self.ans
    
      

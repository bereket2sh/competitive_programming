# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.ans = float(-inf)
        
        def dfs(node):
            if not node:
                return 0
            
            
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.ans = max(self.ans, node.val, right + node.val, left + node.val, node.val + right + left)
            
            return max(right + node.val, left + node.val, node.val)
        
        dfs(root)
        return self.ans if self.ans != float(-inf) else root.val
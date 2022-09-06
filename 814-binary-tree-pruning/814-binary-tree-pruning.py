# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

""""
    1
null 0
    0  1
    
"""
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            
            if not node:
                return False
            
            left, right = dfs(node.left), dfs(node.right)
            
            if not left:
                node.left = None
            if not right:
                node.right = None
                
            return node.val or left or right
            
        
        return root if dfs(root) else None
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return None
            
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            node.left = r
            node.right = l
            
            return node
        
        dfs(root)
        return root
        
        
        
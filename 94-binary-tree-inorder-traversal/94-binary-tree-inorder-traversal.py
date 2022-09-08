# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = []
        
        res = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            res.append(root.val)
            root = root.right
        
        return res
            
        
        
        
#         res = []
#         def dfs(node):
#             nonlocal res
#             if not node:
#                 return 
#             dfs(node.left)
#             res.append(node.val)
#             dfs(node.right)
            
#         dfs(root)
#         return res
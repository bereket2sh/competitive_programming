# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while  stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            
        return res
        
#         res = []
        
#         def dfs(node):
#             nonlocal res
#             if not node:
#                 return
            
#             res.append(node.val)
#             dfs(node.left)
#             dfs(node.right)
        
#         dfs(root)
            
#         return res
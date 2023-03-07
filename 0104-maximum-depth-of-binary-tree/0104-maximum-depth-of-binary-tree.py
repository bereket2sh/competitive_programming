# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.ans = 0
        
        def dfs(node, height):
            if not node.left and not node.right:
                if height > self.ans:
                    self.ans = height
                return
            if node.left:
                dfs(node.left, height + 1)
            if node.right:
                dfs(node.right, height + 1)
            
        dfs(root, 1)
        return self.ans
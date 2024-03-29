# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node):
            if not node:
                return 0, 0
            
            lSum, lCount = dfs(node.left)
            rSum, rCount = dfs(node.right)
            s = node.val + lSum + rSum
            n = 1 + lCount + rCount
            
            ave = s //n
            if ave == node.val:
                self.ans += 1
                
            return [s, n]
        
        dfs(root)
        return self.ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nums = []
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)
            
        dfs(root)
        
        nums.sort()
        ans = float('inf')
        
        for i in range(1, len(nums)):
            ans = min(ans, nums[i] - nums[i - 1])
            
        return ans
        
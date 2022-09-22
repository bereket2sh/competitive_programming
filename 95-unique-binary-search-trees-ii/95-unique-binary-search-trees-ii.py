# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(nums):
            if not nums:
                return [None]
            
            ans = []
            for i in range(len(nums)): 
                left = dfs(nums[:i])
                right = dfs(nums[i+1:])

                for l in left:
                    for r in right:
                        root = TreeNode(nums[i])
                        root.left = l
                        root.right = r
                        
                        ans.append(root)
                        
            return ans
            
        nums = list(range(1, n+1))
        return dfs(nums)
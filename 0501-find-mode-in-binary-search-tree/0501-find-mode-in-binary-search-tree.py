# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(int)
        
        def dfs(node):
            if not node:
                return
            
            dic[node.val] += 1
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        
        max_ = max(dic.values())
        
        ans = []
        for a, b in dic.items():
            if b == max_:
                ans .append(a)
        return ans
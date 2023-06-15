# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        ans = 1
        cur = -inf
        level = 1
        
        que = deque([root])
        
        while que:
            tmp = 0
            for i in range(len(que)):
                node = que.popleft()
                if node:
                    tmp += node.val
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
                    
                    
            if tmp > cur:
                ans = level
                cur = tmp  
            level += 1
            
        return ans
                
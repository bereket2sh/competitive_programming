# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        que = deque([root])
        null = False
        
        while que:
            node = que.popleft()
            
            if not node:
                null = True
            else:
                if null:
                    return False
                
                que.append(node.left)
                que.append(node.right)
            
        return True
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        que = deque([(root, 1)])
        width = 0
        
        while que:
            left = que[0][1]
            right = que[-1][1]
            
            width = max(width, right - left + 1)
            
            new_level = deque()
            while que:
                node, ind = que.popleft()
                
                if node.left: new_level.append((node.left, ind*2))
                if node.right: new_level.append((node.right, ind*2 + 1))
                    
            que = new_level
            
        return width
        
       
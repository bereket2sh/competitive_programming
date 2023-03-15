# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        self.heigh = 0
        def dfs(node, depth):
            if not node.left and not node.right:
                self.heigh = max(self.heigh, depth)
                
            if node.left: 
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)
                
        dfs(root, 1)
   
        
        que = deque([root])
        
        for i in range(self.heigh - 1):
            for j in range(len(que)):
                if que[j] == None:
                    return False
            
            new_level = deque()
            while que:
                node = que.popleft()
                if node:
                    new_level.append(node.left if node.left else None)
                    new_level.append(node.right if node.right else None)
                    
            que = new_level
            
      
        nonePos = []
        numPos = []
        for y in range(len(que)):
            if not que[y]:
                nonePos.append(y)
            else:
                numPos.append(y)
                
        if not nonePos:
            return True
        return min(nonePos) > max(numPos)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        que = deque([root])
        
        while que:
            i = 0
            j = len(que) - 1
            while i < j :
                if que[i] == None and que[j] == None:
                    i += 1
                    j -= 1
                    continue
                elif que[i] == None or que[j] == None: return False
                elif que[i].val != que[j].val:
                    return False
                i += 1
                j -= 1
            # print(que)
            # print()
            newLevel = deque()
            while que:
                node = que.popleft()
                if node:
                    newLevel.append(node.left if node.left else None)
                    newLevel.append(node.right if node.right else None)  
                    
            que = newLevel
        
        return True
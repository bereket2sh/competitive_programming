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
            i , j = 0, len(que) - 1
            
            while i < j :
                if not que[i] and que[j]:
                    return False
                elif que[i] and not que[j]:
                    return False
                elif not que[i] and not que[j]:
                    i +=  1
                    j -= 1
                    continue
                elif que[i].val != que[j].val:
                    return False
                i +=  1
                j -= 1
                
            temp = deque()

            while que:
                node = que.popleft()

                if node:
                    temp.append(node.left)
                    temp.append(node.right)

            que = temp
                
        return True
            
            
                      
        

            
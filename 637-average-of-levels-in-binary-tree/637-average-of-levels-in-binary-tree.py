# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        qeue = deque()
        qeue.append(root)
        ans = []
        
        while qeue:
            
            sumLevel = 0
            length = len(qeue)
            for _ in range(len(qeue)):
                temp = qeue.popleft()
                sumLevel += temp.val
                
                if temp.right:
                    qeue.append(temp.right)
                if temp.left:
                    qeue.append(temp.left)
            
            ans.append(sumLevel/length)
                
        return ans
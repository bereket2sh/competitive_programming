# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        que = deque()
        que.append(root)
        res = []
        
        while que:
            n = len(que)
            temp = []
            newQue = deque()
            for _ in range(n):
                node = que.popleft()
                temp.append(node.val)
                if node.left:
                    newQue.append(node.left)
                if node.right:
                    newQue.append(node.right)
                    
            que = newQue
            res.append(temp)
            
        res.reverse()
        return res
            
        # low, high = 0, len(res)-1
        # while low < high:
        #     t = res[high]
        #     res[high] = res[low]
        #     res[low] = t
        #     low += 1
        #     high -= 1
        # return res
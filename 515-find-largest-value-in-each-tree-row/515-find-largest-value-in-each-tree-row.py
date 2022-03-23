# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            var = -inf
            q = deque()
            while queue:
                temp = queue.popleft()
                var = max(var,temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            queue = q
            res.append(var)
        return res
        
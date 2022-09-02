# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        def helper(node, paths):
            nonlocal res
            
            if not node.left and not node.right:
                if sum(paths) == targetSum:
                    res.append(paths)
                return
            
            if node.left:
                helper(node.left, paths + [node.left.val])
            if node.right:
                helper(node.right, paths + [node.right.val])
                
        
        paths = [root.val]
        helper(root, paths)
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True
        def rec(node):
            nonlocal res
            leftMin, leftMax, rightMin, rightMax = -inf, -inf, inf, inf
            if node.left:
                leftMin, leftMax = rec(node.left)
            if node.right:
                rightMin, rightMax = rec(node.right)
            if not leftMax < node.val < rightMin:
                res = False
            if leftMin == -inf:
                leftMin = node.val
            if rightMax == inf:
                rightMax = node.val
            return (leftMin, rightMax)
        rec(root)
        return res
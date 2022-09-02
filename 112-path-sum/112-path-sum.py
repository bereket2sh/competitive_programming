# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def helper(node, pathSum):
            if not node:
                return False
            if not node.left and not node.right:
                return pathSum == targetSum
            
            if node.left and not node.right:
                return helper(node.left, pathSum + node.left.val) 
            if node.right and not node.left:
                return  helper(node.right, pathSum + node.right.val)
            else:
                return helper(node.left, pathSum + node.left.val) or helper(node.right, pathSum + node.right.val)
        return helper(root, root.val)
            
        
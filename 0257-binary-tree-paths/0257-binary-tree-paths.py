# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        def dfs(node, res, path):
            if not node.left and not node.right:
                res.append(path)
                
            
            if node.left:
                dfs(node.left, res, path + "->" + str(node.left.val))
                
            if node.right:
                dfs(node.right, res, path + "->" + str(node.right.val))
                
            return res
        
        return dfs(root, [], str(root.val))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(arr):
            if not arr:
                return None
            
           
            root_val = arr[0]
            root = TreeNode(root_val)
            
            i = 1
            while i < len(arr) and arr[i] < root_val:
                i += 1
            
            root.right = dfs(arr[i : ])
            root.left = dfs(arr[1 : i])
            
            
            return root
        
        
        return dfs(preorder)
# [1, 5, 7, 8, 10, 12]
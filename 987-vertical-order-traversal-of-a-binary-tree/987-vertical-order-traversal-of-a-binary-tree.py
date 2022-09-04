# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        
        def dfs(node,row,col):
            nonlocal arr
            arr.append([col,row,node.val])
            if not node.left and not node.right:
                return
            
            
            if node.left:
                dfs(node.left, row+1, col-1)
            if node.right:
                dfs(node.right, row+1,col+1)
                
        dfs(root,0,0)
        arr.sort()
        res = []
        j = 0
        while j < len(arr):
            temp = []
            columen, index = arr[j][0], j
            while index < len(arr) and arr[index][0] == columen:
                temp.append(arr[index][2])
                index += 1
            res.append(temp)
            j = index
        
        return res
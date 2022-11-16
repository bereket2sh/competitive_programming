# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.nodes = []
        def helper(node):
            if node:
                helper(node.left)
                self.nodes.append(node)
                helper(node.right)
                
        helper(root)
        temp = []
        for node in self.nodes:
            temp.append(node.val)
            
        temp.sort()
        print(temp)
        for i in range(len(self.nodes)):
            self.nodes[i].val = temp[i]
                    
                    
        
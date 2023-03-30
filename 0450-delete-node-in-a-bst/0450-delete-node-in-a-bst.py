# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
       
        if not node: 
            return None

        if node.val == key:
            if not node.right:
                return node.left
            if not node.left:
                return node.right

            if node.left and node.right:
                temp = node.right
                while temp.left:
                    temp = temp.left
                node.val = temp.val
                node.right = self.deleteNode(node.right, node.val)

        elif node.val > key:
            node.left = self.deleteNode(node.left, key)

        else:
            node.right = self.deleteNode(node.right, key)
                
       
        return node
    
    
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        s1, s2, res = [root], [], []
        
        while s1:
            node = s1.pop()
            s2.append(node)
            for child in node.children:
                s1.append(child)
                
        while s2:
            node = s2.pop()
            res.append(node.val)
        
        return res
        
        
        
        
        
        
        
        
#         res = []
        
#         def dfs(node):
#             nonlocal res
#             if not node:
#                 return
            
#             for child in node.children:
#                 dfs(child)
                
#             res.append(node.val)
            
#         dfs(root)
#         return res
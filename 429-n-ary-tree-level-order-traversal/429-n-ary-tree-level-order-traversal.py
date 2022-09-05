"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return root
        que = deque()
        que.append(root)
        res = []
        
        while que:
           
            newQue = deque()
            temp = []
            while que:
                
                node = que.popleft()
                temp.append(node.val)
                for child in node.children:
                    newQue.append(child)
            
            que = newQue
            res.append(temp)
        return res
                
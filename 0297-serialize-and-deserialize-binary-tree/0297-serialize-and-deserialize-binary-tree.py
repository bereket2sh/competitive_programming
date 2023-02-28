# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def dfs(self, node, serialized_path):
        if not node:
            serialized_path.append('#,')  # we use '#' to represent null
            return None
        serialized_path.append(str(node.val) + ",")
        self.dfs(node.left, serialized_path)
        self.dfs(node.right, serialized_path)
        
    
    def build_tree(self):
        curr = self.data[self.idx]
        self.idx += 1
        if self.idx == len(self.data) or curr == '#':
            return None
        
        left_subtree = self.build_tree()
        right_subtree = self.build_tree()
        curr_root = TreeNode(int(curr), left_subtree, right_subtree)
            
        return curr_root
    

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialized_path = []
        self.dfs(root, serialized_path)
        return "".join(serialized_path)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.idx = 0
        self.data = data.split(',')[:-1]  # when we split "2,1,3," it returns [2, 1, 3, ""]
        return self.build_tree()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
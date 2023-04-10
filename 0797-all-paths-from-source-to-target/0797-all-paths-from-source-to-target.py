class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        self.n = len(graph)
        ans = []
      
        
        def helper (node, path):
            if node == self.n - 1:
                ans.append(path.copy())
                return 
            
           
            for nei in graph[node]:
                path.append(nei)
                helper(nei, path)
                
                path.remove(nei)
            
        helper(0, [0])
        
        return ans
                
                
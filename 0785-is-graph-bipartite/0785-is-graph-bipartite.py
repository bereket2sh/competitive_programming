class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.ans = True
        
        color = [-1] * len(graph)
        
        def dfs(node):
            
            seen.add(node)
            
            for child in graph[node]:
                if child not in seen:
                    color[child] = 1 - color[node]
                    dfs(child)
                    
                else:
                    if color[child] == color[node]:
                        self.ans = False
                        
        seen = set()
        
        for i in range(len(graph)):
            if i not in seen:
                dfs(i)
                
        return self.ans
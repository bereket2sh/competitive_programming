class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        
        def dfs(node, c):
            color[node] = c
            for nei in adj[node]:
                if color[nei] == c:
                    return False
                if color[nei] == -1:
                    
                    if not dfs(nei, 1 - c):
                        return False
                
            return True
            
        
        
        
        color = [-1] * (n + 1)
        adj = [[] for i in range((n+ 1)) ]
        
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
            
        print(adj)
        for i in range(1, (n + 1)):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
                
        return True
            
        
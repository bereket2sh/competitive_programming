class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        
        
        
        def dfs(node):
            
            visited.add(node)
            path.add(node)
            
            for child in graph[node]:
                if child not in path:
                    dfs(child)
                    
        visited = set()
        
        var = 0
        ans = 0
        for i in range(n):
            if i not in visited:
                path = set()
                dfs(i)
                ans += var * len(path)
                var += len(path)
                
        return ans
                
                
                
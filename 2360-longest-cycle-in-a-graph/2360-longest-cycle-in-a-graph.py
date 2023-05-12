class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(list)
        
        for i, edge in enumerate(edges):
            graph[i].append(edge)
        
        self.ans = -1
        
        arr = [0] * len(edges)
        prev_visited = set()
        
        def dfs(node, val):
            # print(node)
            if node in prev_visited:
                return
            
            
            arr[node] = val
            visited.add(node)
            prev_visited.add(node)
            
            for child in graph[node]:
                if child in visited:
                    # print("here")
                    self.ans = max(self.ans, val - arr[child] + 1)
                    return 
                dfs(child, val + 1)
                
                
        for num in range(len(edges)):
            if num not in prev_visited:
                visited = set()
                dfs(num, 1)
                
        return self.ans
            
        
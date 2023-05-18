class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for a, b, d in roads:
            graph[a].append([b,d])
            graph[b].append([a, d])
        # print(graph)
        self.ans = float('inf')
        
        def dfs(node, distance):
            self.ans = min(self.ans, distance)
            for child, d in graph[node]:
                if (child, node) not in seen and (node, child) not in seen:
                    seen.add((node, child))
                    dfs(child, d)
        
        seen = set()      
        dfs(1, float('inf'))
        return self.ans
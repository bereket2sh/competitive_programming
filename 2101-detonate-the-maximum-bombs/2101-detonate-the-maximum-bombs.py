class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j:
                    x = (bombs[i][0] - bombs[j][0])
                    y = (bombs[i][1] - bombs[j][1])
                    distance = math.sqrt(x**2 + y**2)
                    if distance <= bombs[i][2]:
                        graph[i].append(j)
        
        output = 0
        def dfs(node, visited):
            for child in graph[node]:
                if child not in visited:

                    visited.add(child)
                    dfs(child, visited)
                    
        for i in range(len(bombs)):
            visited = set([i])
            dfs(i, visited)
            output = max(output, len(visited))

        return output

        
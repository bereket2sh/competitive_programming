class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        
        for ind in range(1, len(parent)):
            graph[parent[ind]].append(ind)
            
        ans = 1
        
        def dfs(vertex):
            nonlocal ans
            if not graph[vertex]:
                return s[vertex]
            
            
            temp = []
            for nei in graph[vertex]:
                var = dfs(nei)
                # print(var)
                if var[-1] != s[vertex]:
                    temp.append(var)
            # print(temp)       
            if not temp:
                return s[vertex]
            if len(temp) == 1:
                ans = max(ans, len(temp[0] + s[vertex]))
                return temp[0] + s[vertex]
            
            temp = sorted(temp, key = lambda x:len(x))
            ans = max(ans, len(temp[-1] + temp[-2] + s[vertex]))
            return temp[-1] + s[vertex]
                    
        # print(graph)
        dfs(0)
        return ans
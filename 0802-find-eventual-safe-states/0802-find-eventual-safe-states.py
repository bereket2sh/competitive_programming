class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        dict_graph = defaultdict(list)
        for i, g in enumerate(graph):
            for val in g:
                dict_graph[i].append(val)
        
        def dfs(node):
            if colors[node] == 2:
                return False
            if colors[node] == 1:
                return True
            
            colors[node] = 1
            
            for neig in dict_graph[node]:
                if dfs(neig):
                    return True
                 
   
            colors[node] = 2
            return False
            
            
        colors = [0] * len(graph)
        ans = []
        
        for i in range(len(graph)):
            safe = dfs(i)
            if not safe:
                ans.append(i)
                
        # ans = sorted(list(set(ans)))
        return ans
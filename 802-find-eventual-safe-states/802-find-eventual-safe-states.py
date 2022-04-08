class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #color 0 is not vistied ,color 1 is visited(safe) and color 2 is in cylcle(check)
        
        def dfs(num):  
            if color[num] == 2:
                return False
            if color[num] == 1:
                return True
            color[num] = 2
            for i in graph[num]:
                if dfs(i) == False:
                       return False
            
            color[num] = 1
            return True

        color = [0]*len(graph)
        output = []
        for i in range(len(graph)):
            if dfs(i): output.append(i)
        
        return output
        
        
        
#         node = defaultdict(list)
#         out_degree = defaultdict(int)
#         queue = deque()
#         res = []
        
#         for i in range(len(graph)):
#             out_degree[i] = len(graph[i])
#             if out_degree[i] == 0:
#                 queue.append(i)
#             for j in graph[i]:
#                 node[j].append(i)
        
#         while queue:
#             curr = queue.popleft()
#             res.append(curr)
#             for num in node[curr]:
#                 out_degree[num] -= 1
#                 if out_degree[num] == 0:
#                     queue.append(num)
        
#         res.sort()
#         return res
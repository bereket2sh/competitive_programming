class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda: defaultdict(list))
        group_graph = defaultdict(list)
        
        count = m
        for i in range(len(group)):
            if group[i] == -1:
                group[i] = count
                count += 1
                
        for val, gr in enumerate(group):
            if val not in graph[gr]:
                graph[gr][val] = [[], [0]]
            if gr not in group_graph:
                group_graph[gr] = [[], [0]]

            for bef in beforeItems[val]:
                if group[bef] == gr:
                    if bef in graph[gr]:
                        graph[gr][bef][0].append(val)
                    else:
                        graph[gr][bef] = [[val], [0]]

                    graph[gr][val][1][0] += 1

                else:
                    if group[bef] not in group_graph:
                        group_graph[group[bef]] = [[gr], [0]]

                    else:
                        group_graph[group[bef]][0].append(gr)

                    group_graph[gr][1][0] += 1
                    
        def topological(g):
            order = []
            que = deque()
            for key in g.keys():
                if g[key][1][0] == 0:
                    que.append(key)
                    
            while que:
                temp = que.popleft()
                order.append(temp)
                
                for child in g[temp][0]:
                    g[child][1][0] -= 1
                    if g[child][1][0] == 0:
                        que.append(child)
                        
            return order         
            
        ans = []
        var = topological(group_graph)
        
        for i in range(len(var)):
            temp = topological(graph[var[i]])
            for t in temp:
                ans.append(t)
                
        return ans if len(ans) == len(group) else []
            
            
                        
            
            
                        
            
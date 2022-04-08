class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        node = defaultdict(list)
        out_degree = defaultdict(int)
        queue = deque()
        res = []
        
        for i in range(len(graph)):
            out_degree[i] = len(graph[i])
            if out_degree[i] == 0:
                queue.append(i)
            for j in graph[i]:
                node[j].append(i)
        
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for num in node[curr]:
                out_degree[num] -= 1
                if out_degree[num] == 0:
                    queue.append(num)
        
        res.sort()
        return res
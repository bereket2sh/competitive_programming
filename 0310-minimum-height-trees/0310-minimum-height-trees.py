class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = [0] * n
        
        for a , b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
            
        qeue = deque()
        
        for i, val in enumerate(indegree):
            if val == 1:
                qeue.append(i)
                
        prev = [0]
        while qeue:
            prev = qeue.copy()
            
            n = len(qeue)
            for i in range(n):
                node = qeue.popleft()
                
                for child in graph[node]:
                    indegree[child] -= 1
                    if indegree[child] == 1:
                        qeue.append(child)
                        
        
        return prev
            
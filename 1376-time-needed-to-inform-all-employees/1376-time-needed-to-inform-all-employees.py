class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        
        graph = defaultdict(list)
        
        for ind, val in enumerate(manager):
            if val != -1:
                graph[val].append(ind)
                
        self.answer = 0
        
        def dfs(node, time):
            if not graph[node]:
                self.answer = max(self.answer, time)
                
            for child in graph[node]:
                dfs(child, time + informTime[node])
                
        dfs(headID, 0)
        
        return self.answer
                
            
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(int)
        
        
        for a, b in edges:
            graph[b] += 1
            
        res = []
        
        for i in range(n):
            if graph[i] == 0:
                res.append(i)
                
        return res
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        ans = set(range(n)) - set(j for i, j in edges)
        
        return list(ans)
            
        
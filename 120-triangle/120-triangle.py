class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cach = {}
        def dfs(i,j):
            if i == len(triangle)-1:
                if (i,j) in cach:
                    return cach[(i,j)]
                cach[(i,j)] = triangle[i][j]
                return triangle[i][j]
            if (i,j) in cach:
                return cach[(i,j)]
            cach[(i,j)] = triangle[i][j] + min(dfs(i+1,j),dfs(i+1,j+1))
            return cach[(i,j)]
        return dfs(0,0)
        
        
        
#         n = len(triangle)
#         for i in range(n-2,-1,-1):
#             for j in range(len(triangle[i])):
#                 triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])
#         return triangle[0][0]
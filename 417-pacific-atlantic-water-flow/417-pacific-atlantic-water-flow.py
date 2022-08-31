class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        atlantic, pacific = set(), set()
        def dfs(r,c,visit,prevHeight):
            if (r<0 or r==rows or c<0 or c==cols or (r,c) in visit or heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            dfs(r + 1,c,visit,heights[r][c])
            dfs(r - 1,c,visit,heights[r][c])
            dfs(r,c + 1,visit,heights[r][c])
            dfs(r,c - 1,visit,heights[r][c])
                
        
        
        for c in range(cols):
            dfs(0,c,atlantic,heights[0][c]) # first row 
            dfs(rows-1,c,pacific,heights[rows-1][c]) # last row
            
        for r in range(rows):
            dfs(r,0,atlantic,heights[r][0]) # first col
            dfs(r,cols-1,pacific,heights[r][cols-1]) # last col
            
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in atlantic and (i,j) in pacific:
                    res.append([i,j])
                    
        return res
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dir = [(0,1),(0,-1),(1,0),(-1,0)]
#         visited = set()
        
#         def pacific(r,c):
#             if r <= 0 or c <= 0:
#                 return True
#             if r >= len(heights) or c >= len(heights):
#                 return
#             visited.add((r,c))
            
#             for dr, dc in dir:
#                 newR = r + dr
#                 newC = c + dc
#                 if valid(r,c,newR,newC):
#                     pacific(newR, newC)
                
#         visited = set()    
#         def atlantic(r,c):
#             if r <= 0 or c <= 0:
#                 return 
#             if r >= len(heights) or c >= len(heights):
#                 return True
#             visited.add((r,c))
            
#             for dr, dc in dir:
#                 newR = r + dr
#                 newC = c + dc
#                 if valid(r,c,newR,newC):
#                     pacific(newR, newC)
            
            
#         def valid(r,c,newR, newC):
#             if (newR,newC) not in visited:
#                 if newR>=0 and newC >= 0 and newR < len(heights) and newC < len(heights[0]):
#                     if heights[newR][newC] <= heights[r][c]:
#                         return True
#             return False
               
            
        
#         ans = []
        
#         for i in range(len(heights)):
#             for j in range(len(heights[0])):
#                 if pacific(i,j) and atlantic(i,j):
#                     ans.append([i,j])
#         return ans
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        ans = 0
        for g in grid:
            ans +=  bisect.bisect_left(g[::-1], 0)
        
        return ans
    

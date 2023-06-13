class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        
        for g in grid:
            for i in range(len(grid)):
                tmp = []
                for j in range(len(grid)):
                    tmp.append(grid[j][i])
                    
                ans += g == tmp
                
        return ans
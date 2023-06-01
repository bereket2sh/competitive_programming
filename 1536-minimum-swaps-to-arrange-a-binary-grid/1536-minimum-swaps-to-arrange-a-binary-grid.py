class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        count_zeros = defaultdict(int)
        
        for i in range(n):
            ind = n - 1
            count = 0
            while ind > 0 and grid[i][ind] == 0:
                count += 1
                ind -= 1
                
            grid[i].append(count)
        
        # print(grid) 
        step = 0
        required = n - 1
        
        for i in range(n):
            if grid[i][n] < required:
                flag = True
                
                for j in range(i + 1, n):
                    if grid[j][n] >= required:
                        for z in range(j - 1, i - 1, -1):
                            grid[z], grid[z + 1] = grid[z + 1], grid[z]
                            step += 1
                        
                        
                        flag = False
                        break
                    
                if flag:
                    return -1
                
            required -= 1
                
        return step
        
                        
                
             
                        
                        
        
                
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1:
            return -1
        
        n = len(grid)
        
        que = deque([(0, 0, 1)])
        grid[0][0] = 1
        directions = [[0,1], [1,0],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        
        def valid(row, col):
            return 0 <= row < n and 0 <= col < n and grid[row][col] == 0
        
        while que:
            row, col, step = que.popleft()
            
            
            if row == n - 1 and col == n - 1:
                return step
            
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                
                if valid(new_row, new_col):
                    
                    que.append((new_row, new_col, step + 1))
                    grid[new_row][new_col] = 1
        return -1
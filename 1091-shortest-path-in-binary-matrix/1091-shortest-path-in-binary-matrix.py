class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dir = [[1, 0],[-1, 0], [0, 1], [0, -1], [1,1], [-1, 1], [1, -1], [-1, -1]]
        
        if grid[0][0]  == 1:
            return -1
        
        qeue = deque()
        qeue.append([1, [0, 0]])
        
        ans = float('inf')
        
        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m
        
        visited = set()
        visited.add((0, 0))
        
        while qeue:
            
            
            step, index = qeue.popleft()
            
            if index[0] == n - 1 and index[1] == m - 1:
                if step < ans:
                    ans = step
                    
            else:
                for dr, dc in dir:
                    newRow, newCol = index[0] + dr, index[1] + dc 
                    if inbound(newRow, newCol) and  grid[newRow][newCol]  == 0 and (newRow, newCol) not in visited:
                        qeue.append([step + 1, [newRow, newCol]])
                        visited.add((newRow, newCol))
           
                        
        return ans if ans != float('inf') else -1
                
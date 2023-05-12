class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        que = deque()
        visited = set()
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                flag = False
                if grid[i][j] == 1:
                    flag = True
                    q = deque([(i, j)])
                    visited.add((i,j))
                    
                    while q:
                        row, col = q.popleft()
                        que.append((row, col, 0))
                        for dr, dc in dir:
                            
                            if inbound(row + dr, col + dc) and grid[row + dr][col + dc] == 1 and (row + dr, col + dc) not in visited:
                                
                                q.append((row + dr, col + dc))
                                visited.add((row + dr, col + dc))
                                
                    break
            if flag:
                break

                                
                                
        step = 0
        print(que)
        print("once")
        while que:

            r,c, step = que.popleft()

            for dr, dc in dir:
                row = r + dr
                col = c + dc
                if inbound(row, col) and (row, col) not in visited:
                    if grid[row][col] == 1:
                        return step
                    que.append((row, col, step + 1))
                    visited.add((row, col))
                        
                        
                        
                        
                        
                        
                        # 0 1
                        # 1 0
         # 1 1 1 1 1
         # 1 0 0 0 1
         # 1 0 1 0 1
         # 1 0 0 0 1
         # 1 1 1 1 1
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                
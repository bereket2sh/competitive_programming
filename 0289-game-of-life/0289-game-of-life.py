class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        changed = []
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                liveNei = self.calculateLive(board, [i, j])
                if board[i][j] == 1:
                    if liveNei < 2 or liveNei > 3:
                        changed.append([i, j])
                elif liveNei == 3:
                    changed.append([i, j])
                    
        for x, y in changed:
            board[x][y] = 1 - board[x][y]
    
    
    def calculateLive(self, board, indexes):
        dir = [[1,0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]
        
        
        def inbound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])
        
        liveCell = 0
        for row, col in dir:
            newRow = indexes[0] + row 
            newCol = indexes[1] + col
            if inbound(newRow, newCol) and board[newRow][newCol] == 1:
                liveCell += 1
        
        return liveCell
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(n):
            for j in range(m):
                if i + 1 < n and j + 1 < m:
                    if matrix[i + 1][j + 1] != matrix[i][j]:
                        return False
        return True
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp = matrix[i][j]
                while i < len(matrix) and j < len(matrix[0]):
                    if matrix[i][j] != temp:
                        return False
                    i += 1
                    j += 1
                    
                i = 0
                j = 0
        return True
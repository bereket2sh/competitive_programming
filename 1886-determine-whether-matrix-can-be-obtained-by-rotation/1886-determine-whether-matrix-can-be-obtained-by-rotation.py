class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        
        for _ in range(3):
            newMatrix = []
            for j in range(len(mat)):
                temp = []
                for i in range(len(mat)-1,-1,-1):
                    temp.append(mat[i][j])
                
                newMatrix.append(temp)
            
            mat = newMatrix
            if newMatrix == target:
                return True
        
        return False
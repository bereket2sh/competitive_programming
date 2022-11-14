class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dur = [1, 1, 2, 2]
        
        result = []
        
        while len(result) < rows * cols:
            for i in range(dur[0]):
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    result.append([rStart, cStart])
                    
                cStart += 1
            dur[0] += 2
            
            for i in range(dur[1]):
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    result.append([rStart, cStart])
                    
                rStart += 1
            dur[1] += 2
            
            for i in range(dur[2]):
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    result.append([rStart, cStart])
                    
                cStart -= 1 
            dur[2] += 2
            
            for i in range(dur[3]):
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    result.append([rStart, cStart])
                    
                rStart -= 1 
            dur[3] += 2
            
        return result
            
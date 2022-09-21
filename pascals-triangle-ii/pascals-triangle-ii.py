class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal  = [[1]]
        
        for i in range(1, rowIndex + 1):
            j = 1
            temp = [1]
            while j < len(pascal[i-1]):
                temp.append(pascal[i-1][j-1] + pascal[i-1][j])
                j += 1
                
            temp.append(1)
            pascal.append(temp)
            
        return pascal[-1]
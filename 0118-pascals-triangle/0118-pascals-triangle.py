class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        
        for i in range(1, numRows):
            temp = [1] * (len(pascal[-1]) + 1)
            for j in range(1, len(pascal[-1]) ):
                temp[j] = pascal[-1][j -1] + pascal[-1][j]
            pascal.append(temp)
            
            
        return pascal
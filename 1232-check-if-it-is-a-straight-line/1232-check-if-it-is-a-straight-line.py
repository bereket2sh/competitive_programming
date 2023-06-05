class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n < 3:
            return True
        
        x_dif = coordinates[1][0] - coordinates[0][0]
        y_dif = coordinates[1][1] - coordinates[0][1]
        
        if x_dif == 0:
            for i in range(2, n):
                if coordinates[i][0] - coordinates[i - 1][0] != 0:
                    return False
                
        else:
            slope = y_dif / x_dif
            
            for i in range(2, n):
                x_dif = coordinates[i][0] - coordinates[i - 1][0]
                y_dif = coordinates[i][1] - coordinates[i - 1][1]
                
                if x_dif == 0 or y_dif / x_dif != slope:
                    return False
                
        return True
            
            
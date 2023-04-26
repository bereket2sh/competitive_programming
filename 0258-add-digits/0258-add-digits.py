class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        
        while len(num) > 1:
            temp = 0
            for c in num:
                temp += int(c)
                
            num = str(temp)
            
        return int(num)
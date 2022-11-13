class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i in range(len(columnTitle)):
            x = (ord(columnTitle[i]) - 64)
            y = (26**(len(columnTitle[i + 1: ])))
            result +=  x * y 
            
        return result
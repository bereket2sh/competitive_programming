class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = self.binaryToInteger(a) + self.binaryToInteger(b)
    
        result  = bin(result)
        return result[2:]
        
    def binaryToInteger(self, a) -> int:
        inta = 0
        for i in range(len(a)):
            inta += int(a[i]) * (2**(len(a) - (i + 1)))
        return inta

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        
        i = 1
        
        while i <= n:
            if i % 2 != 0:
                result.append(i)
            else:
                result.append(result[-1] * -1)
            i += 1
                
        if n % 2 != 0:
            result.pop()
            result.append(0)
            
        return result
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
       
        if (log2(n) % 1) == 0:
            return True
        
        t = list(str(n))
        t.sort()
        t.reverse()
        num  = int("".join(t))
        
        t.sort()
        i = 2
        while i <= num + 1:
            
            temp =list( str(i))
            temp.sort()
            
            if temp == t:
                return True
            i *= 2
        return False
        
    
    
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        
        s = list(s)
        step = 0
        
        while 1:
            flag = False
            
            i = 0
            while i < len(s):
                t  = False
                if i + 1 < len(s) and s[i : i + 2] == ["0", "1"]:
                    flag = True
                    s[i], s[i + 1] = s[i + 1], s[i]
                    i += 2
                    
                    t = True
                    
                if not t:
                    i += 1
                
                
         
                    
            if not flag:
                break
            step += 1
                
        return step
                    
            
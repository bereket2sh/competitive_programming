class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = [""]
        
        for c in s:
            temp = []
            if c.isalpha():
                
                for per in result:
                    temp.append(per + c.upper())
                    temp.append(per + c.lower())
                    
            else:
                for per in result:
                    temp.append(per + c)
                    
            result = temp
            
        return result
        
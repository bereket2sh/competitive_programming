class Solution:
    def checkValidString(self, s: str) -> bool:
        _max = 0
        _min = 0
        
        for c in s:
            if c == "(":
                _max += 1
                _min += 1
                
            elif c == ")":
                _max -= 1
                _min = max(_min - 1, 0)
                
            else:
                _max += 1
                _min = max(_min -1 , 0)
                
            if _max < 0:
                return False
            
        return _min == 0
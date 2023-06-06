class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        seen = set()
        _max, _min = max(arr),  min(arr)
        
        if _max - _min == 0:
            return True
        
        if (_max - _min) % (len(arr) - 1) != 0:
            return False
        
        dif = (_max - _min) // (len(arr) - 1)
        
        for val in arr:
            if (val - _min) % (dif) or val in seen:
                return False
            seen.add(val)
            
        return True
    
#     3 5 1
    
#     5 - 1 = 4 // 2 = 2
#     3 - 1 = 2 // 2
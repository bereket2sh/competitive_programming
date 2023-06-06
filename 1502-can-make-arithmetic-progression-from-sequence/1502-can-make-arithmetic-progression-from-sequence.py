class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        _max, _min = max(arr),  min(arr)
        
        if _max - _min == 0:
            return True
        
        if (_max - _min) % (len(arr) - 1) != 0:
            return False
        
        dif = (_max - _min) // (len(arr) - 1)
        
        for i, val in enumerate(arr):
            ind = (val - _min) // dif
            
            if (val - _min) % (dif) or ( i != ind and arr[i] == arr[ind] ):
                return False
            
            arr[i], arr[ind] = arr[ind], arr[i]
            
        return True

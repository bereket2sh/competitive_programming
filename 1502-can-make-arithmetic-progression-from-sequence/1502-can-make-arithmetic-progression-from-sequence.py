class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        max_value, min_value = max(arr),  min(arr)
        n = len(arr)
        
        if max_value - min_value == 0:
            return True
        
        if (max_value - min_value) % (n - 1) != 0:
            return False
        
        dif = (max_value - min_value) // (n - 1)
        
        for i, val in enumerate(arr):
            ind = (val - min_value) // dif
            
            if (val - min_value) % (dif) or ( i != ind and arr[i] == arr[ind] ):
                return False
            
            arr[i], arr[ind] = arr[ind], arr[i]
            
        return True

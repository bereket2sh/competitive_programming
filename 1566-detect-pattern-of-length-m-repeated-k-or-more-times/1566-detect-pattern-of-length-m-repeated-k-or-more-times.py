class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        if k > len(arr):
            return False
        
        p1 = 0
        while p1 < len(arr):
            count = 1
            current = arr[p1 : p1 + m]
            tmp = p1 + m
            while tmp + m <= len(arr) and arr[tmp : tmp + m] == current:
                count += 1
                tmp += m
                
            if count == k:
                return True
            p1 += 1
            
        return False
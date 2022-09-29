class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = []
        for num in arr:
            diff.append([abs(num - x), num])
            
        diff.sort()
        res = []
        for i in range(k):
            res.append(diff[i][1])
        
        res.sort()
        return res
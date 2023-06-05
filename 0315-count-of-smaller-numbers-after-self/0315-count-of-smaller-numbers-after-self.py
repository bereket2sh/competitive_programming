class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        order = []
        ans = [0] * len(nums)
        
        for i, num in enumerate(nums[::-1]):
            ind = bisect.bisect_left(order, num)
            ans[-(i + 1)] = ind
            bisect.insort(order, num)
            
        return ans
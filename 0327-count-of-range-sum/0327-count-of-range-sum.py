class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        
        prefix = []
        ans = 0
        prev_sum = 0
        
        for n in nums:
            prev_sum += n
            
            low = prev_sum - upper
            up = prev_sum - lower
            
            if lower <= prev_sum <= upper:
                ans += 1
                
            low_index = bisect.bisect_left(prefix, low)
            up_index = bisect.bisect_right(prefix, up)
            
            ans += up_index - low_index
            bisect.insort(prefix, prev_sum)
            
            
        return ans
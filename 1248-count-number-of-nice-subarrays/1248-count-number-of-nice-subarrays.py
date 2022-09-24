class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        res = 0
        prefix = {0:1}
        
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total - k in prefix:
                res += prefix[total-k]
                
            if total in prefix:
                prefix[total] += 1
            else:
                prefix[total] = 1
        
        return res
        
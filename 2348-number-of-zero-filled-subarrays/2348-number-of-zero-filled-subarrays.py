class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        
        i = 0
        
        while i < len(nums):
            if nums[i] == 0:
                count = 1
                i += 1
                while i < len(nums) and nums[i] == 0:
                    count += 1
                    i += 1
                    
                res += (count * (count + 1))//2
                
            i += 1
            
        return res
        
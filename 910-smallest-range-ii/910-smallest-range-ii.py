class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = nums[-1] - nums[0]
        for i in range(len(nums)-1):
            new_min = min(nums[0]+k,nums[i+1]-k)
            new_max = max(nums[-1]-k,nums[i]+k)
            res = min(res,new_max-new_min)
            
        return res
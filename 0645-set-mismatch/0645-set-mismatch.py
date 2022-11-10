class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        missed, repeated = 0, 0
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                repeated = nums[i]
                
        nums = set(nums)
        for i in range(1, n + 1):
            if i not in nums:
                missed = i
                
        return [repeated, missed]
            
            
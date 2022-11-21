class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        totalSum = 0
        curSum = sum(nums)
        
        for i in range(1, len(nums) + 1):
            totalSum += i
            
        return totalSum - curSum
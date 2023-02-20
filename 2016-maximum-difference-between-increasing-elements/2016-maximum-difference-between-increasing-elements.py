class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        result = -1
        minNum = nums[0]
        
        for i in range(len(nums)):
            if nums[i] > minNum:
                result = max(result, nums[i] - minNum)
            elif nums[i] < minNum:
                minNum = nums[i]
                
        return result
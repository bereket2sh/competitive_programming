class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for j in range(1, len(nums)):
            ind = j
            while ind > 0 and nums[ind] < nums[ind - 1]:
                nums[ind], nums[ind - 1] = nums[ind - 1], nums[ind]
                ind -= 1
                
                
        
            
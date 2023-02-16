class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = [0] * (len(nums))
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                pre[i] = nums[i]
                
            else:
                pre[i] = max(nums[i], nums[i] + pre[i + 1])
                
        return max(pre)
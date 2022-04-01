class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            temp = res[i]
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    temp = max(temp,res[i]+res[j])
            res[i] = temp
        return max(res)
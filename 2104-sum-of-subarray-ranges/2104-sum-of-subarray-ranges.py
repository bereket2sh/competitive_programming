class Solution:
    #space,time = O(1),O(n^2)
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-1):
            max_num = nums[i]
            min_num = nums[i]
            for j in range(i+1,len(nums)):
                max_num = max(nums[j],max_num)
                min_num = min(nums[j],min_num)
                res += max_num - min_num
        return res

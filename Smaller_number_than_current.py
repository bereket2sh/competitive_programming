class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        n = len(nums)
        count =0
        for i in range(0,n):
            for j in range(0,n):
                if(nums[i]>nums[j]):
                    count +=1
            ans[i] = count
            count = 0
        return ans

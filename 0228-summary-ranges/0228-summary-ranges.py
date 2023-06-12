class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        
        while i < len(nums):
            j = i 
            i += 1
            
            while i < len(nums) and nums[i] - nums[i - 1] < 2:
                i += 1
                
            i -= 1   
            if i == j:
                ans.append(str(nums[i]))
                
            else:
                ans.append(str(nums[j]) + "->" + str(nums[i]))
                
            i += 1
            
        return ans
                
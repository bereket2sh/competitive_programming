class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for j in range(len(nums)-1):
                if(nums[j]>nums[j+1]):
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        output = []
        for n in range(len(nums)):
            if(nums[n]==target):
                output.append(n)
        return output
                
        

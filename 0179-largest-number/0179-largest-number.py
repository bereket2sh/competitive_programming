class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
            
        nums.sort(key = lambda x : len(x))
        # print(nums)
        for i in range(1, len(nums)):
            j = i 
            while j > 0 and int(nums[j] + nums[j - 1]) > int(nums[j - 1] + nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
                        
        # print(nums)
        return "".join(nums) if int("".join(nums)) != 0 else "0"
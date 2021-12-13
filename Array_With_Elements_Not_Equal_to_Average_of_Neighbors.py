class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        ind = 0
        
        ordered = [0] * n
        for i in range(0,n,2):
            ordered[i] = nums[ind]
            ind += 1
        for i in range(1,n,2):
            ordered[i] = nums[ind]
            ind +=1
        return ordered

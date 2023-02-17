class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        res, left = 0, 0
        pos1, pos2 = -1, -1
        for right in range(n):
            if nums[right] == minK:
                pos1 = right
            if nums[right] == maxK:
                pos2 = right
            if nums[right] < minK or nums[right] > maxK:
                left = right + 1
            res += max(0, min(pos1, pos2) - left + 1)
            
        return res
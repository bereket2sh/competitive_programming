class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        ans, running_sum, seen = 0, 0, set()
        
        while right < len(nums):
            if nums[right] not in seen:
                seen.add(nums[right])
                running_sum += nums[right]
                ans = max(ans, running_sum)
                right += 1
                
            else:
                seen.remove(nums[left])
                running_sum -= nums[left]
                left += 1
                
        return ans
            
            
            
        
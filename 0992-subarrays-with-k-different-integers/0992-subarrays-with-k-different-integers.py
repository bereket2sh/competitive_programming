class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(k):
            
            
            counter = defaultdict(int)
            ans = 0
            left = 0
            
            for right in range(len(nums)):
                
                counter[nums[right]] += 1
                
                while len(counter) > k:
                    counter[nums[left]] -= 1
                    
                    if counter[nums[left]] == 0:
                        del counter[nums[left]]
                        
                    left += 1
                    
                ans += right - left + 1
                
            return ans
        
        return helper(k) - helper(k - 1)
            
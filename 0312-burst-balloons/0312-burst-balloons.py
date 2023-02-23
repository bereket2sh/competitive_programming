class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        @cache
        def dfs(i,j):
            #choose one element from the range
            ans = 0
            for k in range(i,j + 1):
                current_pop = nums[k] * nums[i - 1] * nums[j + 1]                
                ans = max(ans,current_pop + dfs(i,k - 1) + dfs(k + 1,j))                        
            return ans
        
        n = len(nums)
        return dfs(1,n - 2)
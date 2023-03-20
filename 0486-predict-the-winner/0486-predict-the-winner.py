class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        @cache
        def dfs(s, e):
            if s == e:
                return nums[s]
            
            a = nums[s] - dfs(s + 1, e)
            b = nums[e] - dfs(s, e - 1)
            
            return max(a, b)
        
        # print(dfs(0, len(nums) - 1) )
        return dfs(0, len(nums) - 1) >= 0
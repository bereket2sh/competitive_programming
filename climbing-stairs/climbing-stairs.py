class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(stair):
            if stair in memo:
                return memo[stair]
            if stair == n:
                return 1
            elif stair > n:
                return 0
            
            memo[stair] =  helper(stair + 1) + helper(stair + 2)
            return memo[stair]
        
        
        return helper(0)
        
        
        
        
        
        
        
        
#         prev = 0
#         cur = 1
#         for i in range(n-1,-1,-1):
#             temp = prev + cur
#             prev = cur
#             cur = temp
        
#         return cur
        
        
        
#         def climb(level):
            
#             if level == n:
#                 return 1
#             elif level > n:
#                 return 0
#             if level in memo:
#                 return memo[level]
            
#             ans = climb(level + 1) + climb(level + 2)
#             memo[level] = ans
#             return ans
#         memo = {}
#         return climb(0)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cach = {}
        
        def dfs(i, curSum):
            if (i, curSum) in cach:
                return cach[(i, curSum)]
            
            if i == len(nums):
                if curSum == target:
                    return 1
                else:
                    return 0
                
            pos = dfs(i+1, curSum + nums[i]) 
            neg = dfs(i+1, curSum - nums[i])
            
            cach[(i, curSum)] = pos + neg
            return cach[(i, curSum)]
        
            
        
        
        return dfs(0, 0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         memo = {}
        
#         def dfs (nums,i,Sum,target):
#             if (i,Sum) in memo:
#                 return memo[(i,Sum)]
#             if i == len(nums) and Sum == target:
#                 return 1
#             elif i == len(nums):
#                 return 0
#             positive = dfs(nums,i+1,Sum + nums[i],target)
#             negative = dfs(nums,i+1, Sum - nums[i], target)
            
#             memo[(i,Sum)] = positive + negative
#             return memo[(i,Sum)]

        
        
#         return dfs(nums,0,0,target)

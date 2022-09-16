class Solution:
    def maximumScore(self, n: List[int], m: List[int]) -> int:
        # memo = {}
        # @cache
        @lru_cache(2000)
        def helper(i,s, e):
            if i == len(m):
                return 0
            # if (i,s,e) in memo:
            #     return memo[(i,s,e)]
            
            opt1 = m[i] * n[s] + helper(i+1, s+1, e)
            opt2 = m[i] * n[e] + helper(i+1, s, e-1)
            # memo[(i,s,e)] = max(opt1,opt2)
            # return memo[(i,s,e)]
            return max(opt1,opt2)
        
        
        return helper(0, 0, len(n)-1)
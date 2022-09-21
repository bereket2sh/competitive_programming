class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        
        def dfs(num):
            if num in cache:
                return cache[num]
            if num < 2:
                return num
            
            res = dfs(num-1) + dfs(num-2)
            cache[num] = res
            return res
        
        return dfs(n)
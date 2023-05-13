class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        self.modulo = 10 ** 9 + 7
        memo = defaultdict(int)
        
        def dp(num):
            if num in memo:
                return memo[num]
            
            if num > high:
                return 0
            if low <= num <= high:
                memo[num] = 1
                memo[num] += dp(num + zero) + dp(num + one)
                return memo[num] % self.modulo
            
           
            memo[num] += dp(num + zero) + dp(num + one)
            memo[num] = memo[num] % self.modulo
            
            return memo[num] 
        
        return dp(0)
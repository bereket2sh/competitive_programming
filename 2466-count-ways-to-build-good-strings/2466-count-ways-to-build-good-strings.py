class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        self.modulo = 10 ** 9 + 7
        @cache
        def dp(num):
            if num > high:
                return 0
            if low <= num <= high:
                val = 1
                val += dp(num + zero) + dp(num + one)
                return val % self.modulo
            
            ans = 0
            ans += dp(num + zero) + dp(num + one)
            
            return ans % self.modulo
        
        return dp(0)
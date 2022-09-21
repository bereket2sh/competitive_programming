class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = self.power(x, abs(n))
        
        if n < 0:
            return 1/ans
        return ans
    
    def power(self,x,n):
        if n == 0:
            return 1
        if n == 1:
            return x

        half = self.power(x,n//2)

        ans = half * half

        if n % 2 != 0:
            ans *= x
        return ans
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        sign = 1
        ans = ""
        for i, n in enumerate(s):
            if (n == "+" and i != 0) or (n == "-" and i != 0):
                break
            if n == "-":
                sign *= -1 
            elif n == "+":
                continue
            
            elif n.isdigit():
                ans += n
            else:
                break
                
        if not ans: return 0
        
        ans = sign * int(ans)
        if ans > (2**31 - 1):
            return 2 ** 31 - 1
        if ans < (-2 ** 31):
            return -2 ** 31
                
        return ans
                
            
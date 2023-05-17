class Solution:
    def myAtoi(self, s: str) -> int:
        state = 0
       
        sign = 1
        ans = 0
        inc = 0
        for i, n in enumerate(s):
            if (n == "+" and i != 0 and state != 0) or (n == "-" and i != 0 and state != 0):
                break
            elif n == "-":
                sign *= -1
                state += 1
            elif n == "+":
                state += 1
                continue
            
            elif n.isdigit():
                state += 1
                ans = ans * 10 + int(n)
            elif n == " " and state == 0:
                continue
            else:
                break
        
     
        ans = sign * int(ans)
        if ans > (2**31 - 1):
            return 2 ** 31 - 1
        if ans < (-2 ** 31):
            return -2 ** 31
                
        return ans
                
            
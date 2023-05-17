class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        else:
            sign = 1
        
        # digits = [str(i) for i in range(0, 10)]
        result = 0
        for c in s:
            if not c.isdigit():
                break
            else:
                result = result*10 + int(c)
        
        result = sign*result
        UPPER_LIMIT = 2**31 - 1
        LOWER_LIMIT = -2**31
        if result < LOWER_LIMIT:
            return LOWER_LIMIT
        elif result > UPPER_LIMIT:
            return UPPER_LIMIT
        else:
            return result
                
            
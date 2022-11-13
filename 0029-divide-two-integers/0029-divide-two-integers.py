class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        d = dividend if dividend > 0 else -1 * dividend
        di = divisor if divisor > 0 else - 1 * divisor
        
        
        count = 0
        
        
        while d >= di:
            temp = di
            c = 1
            
            while d >= temp:
                d -= temp
                count += c
                temp += temp
                c += c
            
            
            
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            return -1 * count if -1 * count > -2147483647 else -2147483648
        
        return  min(2147483647, count)
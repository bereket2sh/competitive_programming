class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        ans = 0
        for i in range(32):
            a_val, b_val, c_val = (a >> i) & 1, (b >> i) & 1, (c >> i) & 1
            # print(a_val, b_val, c_val)
            if c_val:
                ans += (a_val == 0 and b_val == 0)
            else:
                ans += a_val
                ans += b_val
                
        return ans
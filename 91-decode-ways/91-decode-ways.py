class Solution:
    def numDecodings(self, S: str) -> int:
        @cache
        def dfs(i):
            if i == len(S):
                return 1
            if S[i] == "0":
                return 0

            res = dfs(i+1)

            if (i+1) < len(S) and "10" <= S[i] + S[i+1] <= "26":
                res += dfs(i+2)

           
            return res
            
        return dfs(0)  
    
  
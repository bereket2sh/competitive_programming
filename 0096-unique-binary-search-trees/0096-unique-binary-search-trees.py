class Solution:
    def numTrees(self, n: int) -> int:
        
        memo = {}
        
        def countTree(n, memo):
            if n <= 1:
                return 1
            
            result = 0
            
            if n in memo:
                return memo[n]
            
            else:
                for i in range(1, n + 1):

                    left = countTree(i - 1, memo)
                    right = countTree(n - i, memo)

                    result += left * right
                    memo[n] = result
                    
                return result
        
        return countTree(n, memo)
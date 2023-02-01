class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1] + mat[i][j] - dp[i][j]
                
        res = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                row1, row2 = max(0, i - k), min(i + k, m-1)
                col1, col2 = max(0, j - k), min(j + k, n-1)
                res[i][j] = dp[row2 + 1][col2 + 1] - dp[row1][col2 + 1] - dp[row2 + 1][col1] + dp[row1][col1]
        
        return res
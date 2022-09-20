class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:

        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1
        return max(max(row) for row in memo)
        
        
        
        
        
        
        
        
        
        
        
        
        #         N, M = len(nums1), len(nums2)
#         dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
#         res = 0
        
#         for i in range(N-1, -1, -1):
#             for j in range(M-1, -1, -1):
#                 if nums1[i] == nums2[j]:
#                     dp[i][j] = 1 + dp[i + 1][j + 1]
                    
#                 res = max(res, dp[i][j])
                
#         return res
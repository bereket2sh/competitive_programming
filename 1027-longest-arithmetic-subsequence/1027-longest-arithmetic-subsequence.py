class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp=collections.defaultdict(dict)
        maxi=1
        for i in range(len(nums)):
            for j in range(i):
                diff=nums[i]-nums[j]
                if diff not in dp[j]:
                    dp[j][diff]=1
                if diff not in dp[i]:
                    dp[i][diff]=0
                dp[i][diff]=max(dp[i][diff],dp[j][diff]+1)
                maxi=max(maxi,dp[i][diff])
        return maxi
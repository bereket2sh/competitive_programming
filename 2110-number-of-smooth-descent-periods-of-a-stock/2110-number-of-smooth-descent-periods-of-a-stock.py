class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        prev = 1
        ans = 1
        for i in range(1,len(prices)):
            if prices[i-1] - 1 == prices[i]:
                prev += 1
                ans += prev
            else:
                prev = 1
                ans += prev
        return ans
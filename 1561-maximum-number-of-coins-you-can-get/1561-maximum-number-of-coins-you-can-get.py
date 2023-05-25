class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        i = 0
        k = -2
        ans = 0
        while i < len(piles)//3:
            ans += piles[k]
            k -= 2
            i += 1
            
        return ans
    

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans , prev = 0, 0
        
        for n in gain:
            prev += n
            ans = max(ans, prev)
            
        return ans
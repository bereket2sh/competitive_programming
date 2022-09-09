class Solution:
    def numberOfWeakCharacters(self, mat: List[List[int]]) -> int:
        mat.sort(key = lambda x: (-x[0], x[1])) #sort in decending order of attack and increasing of defe
        
        ans, curMax = 0, 0
        
        for a, d in mat:
            if d < curMax:
                ans += 1
            
            curMax = max(curMax, d)
            
        return ans
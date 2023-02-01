class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = float('inf')
        
        for j in range(len(blocks)):
            operation = 0
            black = 0

            i = j
            
            while i < len(blocks) and black < k:
                if blocks[i] == "W":
                    operation += 1
                black += 1
                i += 1
                
            if black == k:
                ans = min(ans, operation)
                
        return ans
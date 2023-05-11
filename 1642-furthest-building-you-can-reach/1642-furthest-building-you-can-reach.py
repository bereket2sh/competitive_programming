class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        prev_height = []
        
        for i in range(len(heights) - 1):
            dif = heights[i + 1] - heights[i]
            
            if dif > 0:
                if bricks >= dif:
                    bricks -= dif
                    heappush(prev_height, -dif)
                    
                else:
                    if ladders:
                        if prev_height and -prev_height[0] > dif:
                            bricks += -dif - heappop(prev_height)
                            
                            heappush(prev_height, -dif)
                            ladders -= 1
                            
                        else:
                            ladders -= 1
                    else:
                        return i
                    
        return len(heights) - 1 
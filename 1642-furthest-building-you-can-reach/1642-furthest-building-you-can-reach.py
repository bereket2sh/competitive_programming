class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        
        for i in range(len(heights) - 1):
            dif = heights[i + 1] - heights[i]
            
            if dif > 0:
                if bricks >= dif:
                    bricks -= dif
                    heappush(heap, -1 * dif)
                    
                elif ladders > 0:
                    if heap:
                        high = -1 * heappop(heap)
                        heappush(heap, -1 * min(dif, high))
                        
                        bricks += high - min(high, dif)
                        
                    ladders -= 1
                    
                else:
                    return i
                
        return len(heights) - 1 
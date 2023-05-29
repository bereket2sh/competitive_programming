class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        
        new = [[a, b] for a, b in zip(capital, profits)]
        new.sort()
        
        ind = 0
        while ind < len(new) and new[ind][0] <= w:
            heappush(heap, -new[ind][1])
            ind += 1
            
        while heap and k > 0:
            w += -heappop(heap)
            k -= 1
            
            while ind < len(new) and new[ind][0] <= w and k > 0 :
                heappush(heap, -new[ind][1])
                ind += 1
                
        return w
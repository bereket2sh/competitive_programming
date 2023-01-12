class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        res = 0     
        heap = nums
        heapq.heapify(heap)
        
        for i in range(k):
            temp = -1 * heapq.heappop(heap)
            res += temp
            
            temp = math.ceil(temp / 3)
            heapq.heappush(heap, -1 * temp)
            
        return res
        
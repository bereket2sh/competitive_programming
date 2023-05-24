class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        nums = sorted(list(zip(nums1, nums2)), key = lambda n : -n[1])
        
        print(nums)
        ans = 0
        running_sum = 0
        heap = []
        for a, b in nums:
            heappush(heap, a)
            running_sum  += a
            
            if len(heap) > k:
                running_sum -= heappop(heap)
            if len(heap) == k:
                ans = max(ans, running_sum * b)
        
        return ans
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [[nums1[x] + nums2[0], (x, 0)] for x in range(len(nums1)) ]
        
        heapify(heap)
        
        ans = []
        
        while k > 0 and heap:
            sum_, index = heappop(heap)
            ans.append([nums1[index[0]], nums2[index[1]]])
            
            if index[1] + 1 < len(nums2):
                heappush(heap, [nums1[index[0]] + nums2[index[1] + 1], (index[0], index[1] + 1)])
                
            k -= 1
            
        return ans
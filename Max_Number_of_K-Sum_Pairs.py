class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = collections.Counter(nums)
        count = 0
        for i in counter:
            if i*2 == k:
                if counter[i] > 1:
                    count += counter[i]//2
                else:
                    continue
            else:
                if k-i in counter:
                    if counter[k-i] > 0:
                        count += min(counter[i],counter[k-i])
                        counter[i] = 0
                        counter[k-i] = 0
        return count
            

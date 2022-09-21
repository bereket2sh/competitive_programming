class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        memo = []
        
        for i in range(len(nums)):
            var = []
            count = 0
            for j in range(i, len(nums)):
                if nums[j] % p == 0:
                    count += 1
                if count <= k:
                    memo.append([i,j])
                else:
                    break
                
                
        res = set()
        for val in memo:
            temp = tuple(nums[val[0]: val[-1]+1])
            
            res.add(temp)
            
            
        return len(res)
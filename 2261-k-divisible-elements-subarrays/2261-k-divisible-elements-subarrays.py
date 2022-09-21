class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        res = 0
        memo = set()
        
        for i in range(len(nums)):
            temp = []
            s = ""
            for j in range(i, len(nums)):
                temp.append(nums[j])
                count = 0
                s += "," + str(nums[j])
                
                for num in temp:
                    if num % p == 0:
                        count += 1
                       
                
                
                if count <= k and s not in memo:
                    res += 1
                memo.add(s)
           
        return res
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        sumEven = 0
        
        for num in nums:
            if num % 2 == 0:
                sumEven += num
        for q in queries:
            if nums[q[1]] % 2 == 0:
                sumEven -= nums[q[1]]
                nums[q[1]] += q[0]
                if nums[q[1]] % 2 == 0:
                    sumEven += nums[q[1]]
                res.append(sumEven)
                    
            else:
                nums[q[1]] += q[0]
                if nums[q[1]] % 2 == 0:
                    sumEven += nums[q[1]]
                    
                res.append(sumEven)
        return res
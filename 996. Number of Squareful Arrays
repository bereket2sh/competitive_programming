class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        self.answer = set()
        
        def valid(num1,num2):
            x = math.sqrt(num1 + num2)
            
            return math.floor(x) == math.ceil(x)
        def backtrack(arr,visited):
            
            if len(visited) == len(nums):
                self.answer.add(tuple(arr))
            
            for j in range(len(nums)):
                
                if j not in visited and (arr == [] or valid(nums[j],arr[-1]) ):
                    visited.add(j)
                    backtrack(arr + [nums[j]], visited)
                    visited.remove(j)
        backtrack([],set())
        return len(self.answer)

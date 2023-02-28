class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = {}
        degree = 0
        for i, num in enumerate(nums):
            if num in dic:
                dic[num][0] += 1
            else:
                dic[num] = [1]
            dic[num].append(i)
            degree = max(degree, dic[num][0])
        ans = float('inf')
        for key in dic:
            if dic[key][0] == degree:
                ans = min(ans, dic[key][-1] - dic[key][1] + 1)

        return ans
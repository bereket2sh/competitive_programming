class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        result = []
        for key, value in count.items():
            if value == 1:
                result.append(key)

        return result
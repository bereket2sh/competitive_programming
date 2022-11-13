class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        number = "".join(digits)
        number = list(str(int(number) + 1))

        for i in range(len(number)):
            number[i] = int(number[i])
        return number
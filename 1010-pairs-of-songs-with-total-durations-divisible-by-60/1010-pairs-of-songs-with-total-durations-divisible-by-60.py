class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counters = [0] * 60
        for t in time:
            counters[t % 60] += 1

        # Count the number of pairs of songs where their total duration is divisible by 60
        count = 0
        for i in range(1, 30):
            count += counters[i] * counters[60 - i]
        count += (counters[0] * (counters[0] - 1)) // 2
        count += (counters[30] * (counters[30] - 1)) // 2
        return count
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        result = 0
        n = len(word)
        p1 = 0
        while p1 < len(sequence):
            tmp = p1
            count = 0
            while tmp + n <= len(sequence) and sequence[tmp : tmp + n] == word:
                count += 1
                tmp += n
            result = max(result, count)
            p1 += 1
        
        return result
            
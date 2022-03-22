class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #space , time = O(n),O(n)
        count = Counter(s)
        Set = set()
        res, var, total = [],0,0
        for char in s:
            if not Set or char not in Set:
                var += 1
                Set.add(char)
                total += count[char] - 1
            else:
                var += 1
                total -= 1
            if total == 0:
                res.append(var)
                Set = set()
                var = 0
        return res
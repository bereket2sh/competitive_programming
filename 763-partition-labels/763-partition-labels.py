class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #space , time = O(n),O(n)
        count = Counter(s)
        Set = set()
        res, var, total = [],[],0
        for char in s:
            if not Set or char not in Set:
                var.append(char)
                Set.add(char)
                total += count[char] - 1
            else:
                var.append(char)
                total -= 1
            if total == 0:
                res.append(len(var))
                Set = set()
                var = []
        return res
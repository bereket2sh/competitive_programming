class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        dic1 = defaultdict(list)
        dic2 = defaultdict(int)

        for a, b in trust:
            dic1[a].append(b)

            dic2[b] += 1

        for key, value in dic2.items():
            if value == n - 1 and key not in dic1:
                return key
        
        return -1

            
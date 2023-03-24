class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        undirected = defaultdict(list)
        directed = defaultdict(list)

        for u, v in connections:
            directed[u].append(v)
            undirected[u].append(v)
            undirected[v].append(u)
        
        # print(directed)
        # print(undirected)
        queue = deque()
        for neig in undirected[0]:
            queue.append([neig, 0])

        seen = set()
        result = 0

        while queue:
            u, v = queue.popleft()
            if v not in directed[u]:
                result += 1
            seen.add(v)
            for nei in undirected[u]:
                if nei not in seen: 
                    queue.append([nei, u])

        return result
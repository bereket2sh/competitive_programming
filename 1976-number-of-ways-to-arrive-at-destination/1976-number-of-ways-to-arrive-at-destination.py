class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append([v, time])
            graph[v].append([u, time])
        print(graph)
        times = [float('inf')]*n
        ways = [0]*n
        times[0] = 0
        ways[0] = 1
        
        pq = [(0,0)] #shortest time  , city
        
        while pq:
            old_t, u = heappop(pq)
            
            for v,t in graph[u]:
                new_t = old_t + t
                
                if new_t < times[v]:
                    times[v] = new_t
                    ways[v] = ways[u]
                    heappush(pq,(new_t,v))
                elif new_t == times[v]:
                    ways[v] += ways[u]
                    
        mod = 10**9 + 7
        return ways[n-1] % mod
                
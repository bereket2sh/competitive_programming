class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for course, pre in prerequisites:
            if pre in graph:
                graph[pre].append(course)
            else:
                graph[pre] = [course]
        indegree = [0]*numCourses
        for i in graph:
            for j in graph[i]:
                indegree[j] += 1
        print (graph)
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        count = 0
        
        while queue:
            pre = queue.popleft()  # where pre is a course with indegree zero
            count += 1
            if pre in graph:
                for course in graph[pre]:
                    indegree[course] -= 1
                    if indegree[course] == 0:
                        queue.append(course)
        
        return count == numCourses
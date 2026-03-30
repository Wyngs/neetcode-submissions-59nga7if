from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]* numCourses
        adj = [[] for _ in range(numCourses)]

        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1
        
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        courseVisited = 0
        
        while queue:
            course = queue.popleft()
            courseVisited +=1
            for neighbor in adj[course]:
                indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return courseVisited == numCourses
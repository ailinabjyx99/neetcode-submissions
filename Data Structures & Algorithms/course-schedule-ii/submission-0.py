class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = defaultdict(list)
        indegree = [0]*numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
                res.append(i)

        while q:
            course = q.popleft()
            for nxt in graph[course]:
                indegree[nxt]-=1
                if indegree[nxt]==0:
                    q.append(nxt)
                    res.append(nxt)

        return res if len(res)==numCourses else []
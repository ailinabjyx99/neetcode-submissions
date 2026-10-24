class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courselist = defaultdict(list)
        indegree = [0]*numCourses
        for a,b in prerequisites:
            courselist[b].append(a)
            indegree[a]+=1

        q = deque(i for i in range(numCourses) if indegree[i]==0)
        taken = 0

        while q:
            course = q.popleft()
            taken+=1
            for nxt in courselist[course]:
                indegree[nxt]-=1
                if indegree[nxt]==0:
                    q.append(nxt)
        return taken == numCourses

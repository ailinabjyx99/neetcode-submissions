class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)

        q = deque()
        time = 0

        while heap or q:
            time+=1
            if heap:
                cnt = heapq.heappop(heap)+1
                if cnt != 0:
                    q.append((cnt,time+n))
            if q and time == q[0][1]:
                heapq.heappush(heap,q.popleft()[0])

        return time
        
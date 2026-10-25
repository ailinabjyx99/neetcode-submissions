class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        
        heap = [(0,k)]
        dist = {}

        while heap:
            t, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node]=t
            for nxt,w in graph[node]:
                if nxt not in dist:
                    heapq.heappush(heap,(t+w,nxt))
        return max(dist.values()) if len(dist)==n else -1
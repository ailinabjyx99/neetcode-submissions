class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        total = len(edges)
        if total+1!=n:
            return False
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = {0}
        q = deque([0])
        while q:
            node = q.popleft()
            for nxt in graph[node]:
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
        return len(visited)==n
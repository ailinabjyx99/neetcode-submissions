class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        q = deque()
        q.append([0,-1])
        visited.add(0)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        while q:
            node,parent = q.popleft()
            for nxt in graph[node]:
                if nxt==parent:
                    continue
                if nxt in visited:
                    return False
                visited.add(nxt)
                q.append([nxt,node])
        return len(visited)==n
            
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def connected(a,b):
            q = deque([a])
            visited = {a}
            while q:
                current = q.popleft()
                for nxt in graph[current]:
                    if nxt==b:
                        return True
                    if nxt in visited:
                        continue
                    visited.add(nxt)
                    q.append(nxt)
            return False

        
        for a, b in edges:
            if connected(a,b):
                return [a,b]
            else:
                graph[a].append(b)
                graph[b].append(a)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        record = [False]*n

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def explore(start):
            record[start]=True
            q = deque([start])
            while q:
                node = q.popleft()
                for nxt in graph[node]:
                    if record[nxt]==True:
                        continue
                    record[nxt]=True
                    q.append(nxt)
            
        count = 0
        for i in range(n):
            if not record[i]:
                explore(i)
                count+=1
        return count
                
                    
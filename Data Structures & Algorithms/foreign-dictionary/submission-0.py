class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {c:0 for w in words for c in w}
        n = len(words)
        for i in range(n-1):
            w1, w2 = words[i],words[i+1]
            if len(w1)>len(w2) and w1[:len(w2)]==w2:
                return ""
            for j in range(min(len(w1),len(w2))):
                if w1[j]!=w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]]+=1
                    break

        q = deque([c for c in indegree if indegree[c]==0])
        res = []
        while q:
            c = q.popleft()
            res.append(c)
            for nxt in graph[c]:
                indegree[nxt]-=1
                if indegree[nxt]==0:
                    q.append(nxt)
        if len(res)<len(indegree):
            return ""
        return "".join(res)


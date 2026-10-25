class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in sorted(tickets,reverse = True):
            graph[src].append(dst)
        
        res = []

        def dfs(airport):
            while graph[airport]:
                nxt = graph[airport].pop()
                dfs(nxt)
            res.append(airport)
        
        dfs("JFK")
        return res[::-1]


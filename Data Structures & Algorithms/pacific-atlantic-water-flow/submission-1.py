class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights),len(heights[0])
        pac = set()
        atl = set()

        def dfs(r,c,visited):
            if (r,c) in visited:
                return
            visited.add((r,c))

            for dr,dc in ([0,1],[0,-1],[1,0],[-1,0]):
                nr,nc = dr+r,dc+c
                if 0<=nr<rows and 0<=nc<cols and heights[nr][nc]>=heights[r][c]:
                    dfs(nr,nc,visited)
        for r in range(rows):
            dfs(r,0,pac)
            dfs(r,cols-1,atl)
        for c in range(cols):
            dfs(0,c,pac)
            dfs(rows-1,c,atl)
        return [list(p) for p in pac & atl]
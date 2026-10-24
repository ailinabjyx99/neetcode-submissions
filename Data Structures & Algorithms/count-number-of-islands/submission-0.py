class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid),len(grid[0])
        visited = set()
        count=0
        def dfs(r,c):
            if (r,c) in visited:
                return
            if grid[r][c]=="0":
                return
            visited.add((r,c))
            for dr,dc in ([0,1],[0,-1],[1,0],[-1,0]):
                nr,nc = dr+r,dc+c
                if 0<=nr<rows and 0<=nc<cols:
                    dfs(nr,nc)            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in visited:
                    count+=1
                    dfs(r,c)
        return count

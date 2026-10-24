class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        visited = set()

        def dfs(r,c):
            if (r,c) in visited or grid[r][c]==0:
                return 0
            visited.add((r,c))
            area = 1    

            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                if 0<=dr+r<rows and 0<=dc+c<cols:
                    area += dfs(dr+r,dc+c)
            return area
        
        maxarea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    maxarea = max(dfs(r,c),maxarea)
        return maxarea
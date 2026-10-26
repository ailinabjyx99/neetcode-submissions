class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        n = len(grid)
        heap = [(grid[0][0],0,0)] # (cost, row, col)
        visited = set()

        while heap:
            cost,r,c = heapq.heappop(heap)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            if r == n-1 and c == n-1:
                return cost
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr = dr+r
                nc = dc+c
                if 0<=nr<rows and 0<=nc<cols:
                    heapq.heappush(heap,(max(cost,grid[nr][nc]),nr,nc))
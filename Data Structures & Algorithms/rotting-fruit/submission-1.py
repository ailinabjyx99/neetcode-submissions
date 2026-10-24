class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(grid),len(grid[0])
        count = 0
        time = 0
        total = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    total+=1
        while q and count<total:            
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in ([1,0],[-1,0],[0,1],[0,-1]):
                    nr,nc = dr+r,dc+c
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        q.append((nr,nc))
                        grid[nr][nc]=2
                        count+=1
            time+=1
        return time if count==total else -1
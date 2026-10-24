class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board),len(board[0])
        visited = set()

        def dfs(r,c):
            if (r,c) in visited:
                return
            visited.add((r,c))
            board[r][c]="S"

            for dr,dc in ([0,1],[0,-1],[1,0],[-1,0]):
                nr,nc = dr+r,dc+c
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc]=="O":
                    dfs(nr,nc)
        for r in range(rows):
            if board[r][0]=="O":
                dfs(r,0)
            if board[r][cols-1]=="O":
                dfs(r,cols-1)
        for c in range(cols):
            if board[0][c]=="O":
                dfs(0,c)
            if board[rows-1][c]=="O":
                dfs(rows-1,c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                if board[r][c]=="S":
                    board[r][c]="O"
                    
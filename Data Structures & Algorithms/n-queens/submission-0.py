class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)] #initialize
        res = []
        cols = set()
        posdig = set()
        netdig = set()
        def backtrack(row):
            if row==n:
                res.append(["".join(r) for r in board])
                return
            for col in range(n):
                if col not in cols and row+col not in posdig and row-col not in netdig:
                    board[row][col]='Q'
                    cols.add(col)
                    posdig.add(row+col)
                    netdig.add(row-col)
                    backtrack(row+1)
                    board[row][col]='.'
                    cols.remove(col)
                    posdig.remove(row+col)
                    netdig.remove(row-col)
        backtrack(0)
        return res
        

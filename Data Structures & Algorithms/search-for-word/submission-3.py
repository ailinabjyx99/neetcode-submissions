class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board),len(board[0])
        def dfs(r,c,i):
            if i==len(word):
                return True
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c]!=word[i]:
                return False
            board[r][c]='#' #left situation, board[r][c]==word[i]
            for dr,dc in ([1,0],[-1,0],[0,1],[0,-1]):
                if dfs(dr+r,dc+c,i+1):
                    return True
            board[r][c]=word[i]

        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False
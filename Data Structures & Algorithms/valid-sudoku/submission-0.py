class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #维护2个二维数组？还有9个？
        
        rows = [[False]*9 for _ in range(9)]
        cols = [[False]*9 for _ in range(9)]
        boxes = [[False]*9 for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = int(board[r][c])-1
                    box = (r//3)*3+c//3
                    if rows[r][num]==True or cols[c][num]==True or boxes[box][num]==True:
                        return False
                    else:
                        rows[r][num]=True
                        cols[c][num]=True
                        boxes[box][num]=True
        return True

        
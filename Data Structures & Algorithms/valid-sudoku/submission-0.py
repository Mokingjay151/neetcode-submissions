class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizontal = []
        vertical = []
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] in horizontal:
                    return False
                elif board[i][j] != ".":
                    horizontal.append(board[i][j])

                if board[j][i] in vertical:
                    return False
                elif board[j][i] != ".":
                    vertical.append(board[j][i])
            horizontal  = []
            vertical = []
        square = []
        for add in [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6], [6,0],[6,3],[6,6]]:
            for x in range(0, 3):
                for y in range(0, 3):
                    if board[x + add[0]][y + add[1]] in square:
                        return False
                    elif board[x + add[0]][y + add[1]] != ".":
                        square.append(board[x + add[0]][y + add[1]])
            square = []
        return True
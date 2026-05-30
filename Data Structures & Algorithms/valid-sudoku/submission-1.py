class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            empty_set=set()
            for j in range(0,9):
                if board[i][j] != ".":
                    if board[i][j] in empty_set:
                        return False
                    else:
                        empty_set.add(board[i][j])
        for i in range(0,9):
            empty_set=set()
            for j in range(0,9):
                if board[j][i] != ".":
                    if board[j][i] in empty_set:
                        return False
                    else:
                        empty_set.add(board[j][i])
        for i in range(0,9,3):
            for j in range(0,9,3):
                empty_set=set()
                for r in range(3):
                    for c in range(3):
                        if board[i+r][j+c] != ".":
                            if board[i+r][j+c] in empty_set:
                                return False
                            else:
                                empty_set.add(board[i+r][j+c])
        return True
            
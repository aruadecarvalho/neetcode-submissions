class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = defaultdict(bool)

        for r, row in enumerate(board):
            for c in range(len(row)):
                print(r, r % 3)
                print(c, c % 3)
                if (r % 3 == 0) and (c % 3 == 0):
                    block_seen = defaultdict(bool)
                    for i in range(3):
                        for j in range(3):
                            print(r, c)
                            print(r + i, c + j)

                            print("-------")
                            n = board[r + i][c + j]
                            if n == ".":
                                continue

                            if block_seen[n] == True:
                                return False

                            block_seen[n] = True
                
                if row[c] == ".":
                    continue

                row_key = ("row", r, row[c])
                if seen[row_key] == True:
                    return False
                
                col_key = ("col", c, row[c])
                if seen[col_key] == True:
                    return False

                seen[row_key] = True
                seen[col_key] = True

        return True
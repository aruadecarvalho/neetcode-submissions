class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r, row in enumerate(board):
            for c in range(len(row)):
                if (r % 3 == 0) and (c % 3 == 0):
                    for i in range(3):
                        for j in range(3):
                            n = board[r + i][c + j]
                            print(math.floor(r / 3), math.floor(c / 3))
                            if n == ".":
                                continue
                            
                            block_row = math.floor(r / 3)
                            block_col = math.floor(c / 3)
                            block_key = ("block", block_row, block_col, n)

                            if block_key in seen:
                                return False

                            seen.add(block_key)
                
                if row[c] == ".":
                    continue

                row_key = ("row", r, row[c])
                if row_key in seen:
                    return False
                
                col_key = ("col", c, row[c])
                if col_key in seen:
                    return False

                seen.add(row_key)
                seen.add(col_key)

        return True
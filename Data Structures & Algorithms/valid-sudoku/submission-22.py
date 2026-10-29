class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r, row in enumerate(board):
            for c in range(len(row)):
                if row[c] == ".":
                    continue

                block_key = ("block", r // 3, c // 3, row[c])
                row_key = ("row", r, row[c])
                col_key = ("col", c, row[c])
                if block_key in seen or row_key in seen or col_key in seen:
                    return False

                seen.add(block_key)
                seen.add(row_key)
                seen.add(col_key)

        return True
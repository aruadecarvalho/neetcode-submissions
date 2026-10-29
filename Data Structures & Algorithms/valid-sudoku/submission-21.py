class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r, row in enumerate(board):
            for c in range(len(row)):
                if row[c] == ".":
                    continue

                block_key = (
                    "block", 
                    math.floor(r / 3), 
                    math.floor(c / 3), 
                    row[c])
                if block_key in seen:
                    return False

                row_key = ("row", r, row[c])
                if row_key in seen:
                    return False
                
                col_key = ("col", c, row[c])
                if col_key in seen:
                    return False

                seen.add(block_key)
                seen.add(row_key)
                seen.add(col_key)

        return True
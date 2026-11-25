class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_n = 0
        for i, row in enumerate(matrix):
            if row[-1] == target:
                return True
            if row[-1] > target:
                row_n = i
                break
        
        l, r = 0, len(matrix[row_n]) - 1
        row = matrix[row_n]
        while l <= r:
            m = l + ((r - l) // 2)
            print(l, r, m, row_n)
            if row[m] == target:
                print("hey")
                return True
            if row[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False
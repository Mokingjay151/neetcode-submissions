class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m - 1
        while low <= high:
            midrow = (high + low) // 2
            if matrix[midrow][n - 1] < target:
                low = midrow + 1
            elif matrix[midrow][0] > target:
                high = midrow - 1
            else:
                break

        low = 0
        high = n - 1
        while low <= high:
            midcol = (high + low) // 2
            if matrix[midrow][midcol] == target:
                return True
            elif matrix[midrow][midcol] < target:
                low = midcol + 1
            else:
                high = midcol - 1

        return False
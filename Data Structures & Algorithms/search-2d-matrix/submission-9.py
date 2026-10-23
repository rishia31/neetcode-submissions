class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        l = 0
        r = len(matrix[0]) - 1
        for i in range(0, rows):
            l = 0
            r = len(matrix[0]) - 1
            while l <= r:
                sum1 = ((l + r) // 2)
                if matrix[i][sum1] == target:
                    return True
                elif matrix[i][sum1] < target:
                    l = sum1 + 1
                else:
                    r = sum1 - 1
        return False
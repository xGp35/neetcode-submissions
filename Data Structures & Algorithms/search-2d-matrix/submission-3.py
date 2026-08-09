class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        req_row = 0
        # find the row in which this might lie.
        low, high = 0, m-1
        while (low <= high):
            mid = low + (high-low)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                low = mid + 1
                req_row = mid
            else:
                high = mid - 1

        # search within that row.
        low, high = 0, n - 1
        while low <= high:
            mid = low + (high-low)//2
            if matrix[req_row][mid] == target:
                return True
            elif matrix[req_row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
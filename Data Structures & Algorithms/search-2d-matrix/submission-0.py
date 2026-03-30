class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        columns = len(matrix[0])
        rows = len(matrix)
        low = 0
        high = rows - 1
        req_row = -1

        while(low <= high):
            mid = low + (high-low)//2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                low = mid + 1
                req_row = mid
            else:
                 high = mid - 1
        
        low = 0
        high = columns - 1
        while(low <= high):
            mid = low + (high-low)//2

            if matrix[req_row][mid] == target:
                return True
            elif matrix[req_row][mid] < target:
                low = mid + 1
            else:
                 high = mid - 1 

        return False

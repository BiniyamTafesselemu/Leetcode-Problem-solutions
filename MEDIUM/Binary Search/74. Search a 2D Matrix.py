class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        
        # Step 1: Binary search to find the correct row
        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                # Target is in this row
                row = mid
                break
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            return False  # Target is not in any row
        
        # Step 2: Binary search in the found row
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

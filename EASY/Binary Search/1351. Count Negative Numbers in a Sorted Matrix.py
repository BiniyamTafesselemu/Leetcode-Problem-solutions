class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        rows = len(grid)
        
        for i in range(rows):
            # Perform binary search for the first negative number in each row
            l, r = 0, len(grid[0]) - 1
            
            while l <= r:
                mid = (l + r) // 2
                if grid[i][mid] < 0:
                    r = mid - 1  # Move left to find the first negative
                else:
                    l = mid + 1  # Move right
            
            # All elements from index l to the end of the row are negative
            count += len(grid[0]) - l
        
        return count

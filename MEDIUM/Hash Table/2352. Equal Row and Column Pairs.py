from typing import List
from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_count = defaultdict(int)
        
        for row in grid:
            row_count[tuple(row)] += 1
        
        count = 0
        n = len(grid)
        
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))  
            count += row_count[col]  
        
        return count


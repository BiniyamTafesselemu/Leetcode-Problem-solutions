class Solution:
    def reverse(self, x: int) -> int:
        # Handle negative numbers
        sign = -1 if x < 0 else 1
        x *= sign  # Make x positive for processing
        
        reversed_num = 0
        
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        # Restore the sign
        reversed_num *= sign
        
        # Check for overflow
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num

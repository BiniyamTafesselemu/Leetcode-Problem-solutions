class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        prev_value = 0
        for char in reversed(s):
            current_value = d[char]
            if current_value < prev_value:
                ans -= current_value
            else:
                ans += current_value
            prev_value = current_value
        
        return ans

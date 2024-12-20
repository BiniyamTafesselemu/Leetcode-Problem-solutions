class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_len = 0
        seen = set()

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                max_len = max(max_len, r - l + 1)
                r += 1
            else:
                seen.remove(s[l])
                l += 1

        return max_len
    
# ///////////////////    OR    ////////////////////////////////////////////////
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l = 0
        max_length = 0
        
        for r in range(len(s)):
            if s[r] in d and d[s[r]] >= l:
                l = d[s[r]] + 1
            d[s[r]] = r
            max_length = max(max_length, r - l + 1)
        
        return max_length


            


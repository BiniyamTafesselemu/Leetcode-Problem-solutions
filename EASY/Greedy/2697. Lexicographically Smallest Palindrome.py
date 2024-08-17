class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l, r = 0, len(s) - 1
        s_list = list(s)  # Convert to a list for mutability

        while l <= r:
            if s_list[l] != s_list[r]:
                # Replace both characters with the smaller one
                smaller_char = min(s_list[l], s_list[r])
                s_list[l] = smaller_char
                s_list[r] = smaller_char
            l += 1
            r -= 1

        return ''.join(s_list)  # Convert list back to string

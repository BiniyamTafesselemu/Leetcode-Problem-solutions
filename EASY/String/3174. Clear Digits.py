class Solution:
    def clearDigits(self, s: str) -> str:
        ans=""
        for i in s:
            if i.isdigit():
                ans=ans[:-1]
            else:
                ans+=i
        return ans
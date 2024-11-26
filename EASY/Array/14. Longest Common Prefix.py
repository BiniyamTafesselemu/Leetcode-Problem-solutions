class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        strs.sort()
        pointer=0
        while pointer<len(strs[0]) and pointer <len(strs[-1]):
            if strs[0][pointer]!=strs[-1][pointer]:
                break
            else:
                ans+=strs[0][pointer]
            pointer+=1
        return ans
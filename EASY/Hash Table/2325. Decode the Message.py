class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        smalls=97
        ans=""
        d={}
        for i in key:
            if i !=" " and i not in d:
                d[i]=chr(smalls)                
                smalls+=1
        for j in message:
            if j==" ":
                ans += " "
            else:
                ans+=d[j]
        return ans
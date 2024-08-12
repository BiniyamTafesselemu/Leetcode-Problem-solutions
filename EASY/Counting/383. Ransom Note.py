class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1={}
        d2={}
        for i in ransomNote:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
        for j in magazine:
            if j not in d2:
                d2[j]=1
            else:
                d2[j]+=1
        for k in d1:
            if k in d2:
                if d2[k] < d1[k]:
                    return False
                    break
            else:
                return False
                break
        return True
class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        if not s:
            return 0
        
        i=0
        sign=1
        if s[i]=="+":
            i+=1
        elif s[i]=="-":
            i+=1
            sign=-1
        
        ans=0
        while i < len(s):
            curr=s[i]
            if not curr.isdigit():
                break
            else:
                ans=ans*10+int(s[i])
            i+=1
        ans=ans*sign
        if ans < -2**31:
            return -2**31
        elif ans >2**31-1:
            return 2**31-1
        else:
             return  ans 
        
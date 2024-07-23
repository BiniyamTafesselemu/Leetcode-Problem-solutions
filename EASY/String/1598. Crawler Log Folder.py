class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count=0
        for i in logs:
            if i=='../' and count==0:
                continue
            elif i=='../' and count>0:
                count-=1
            elif i=='./':
                continue
            else:
                count+=1
        return count
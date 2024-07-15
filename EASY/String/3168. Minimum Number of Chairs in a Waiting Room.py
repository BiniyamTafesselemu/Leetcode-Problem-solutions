class Solution:
    def minimumChairs(self, s: str) -> int:
        count=0
        max_val=0
        for i in s:
            if i == "E":
                count+=1
                max_val=max(count,max_val)
            else:
                count-=1
        return max_val
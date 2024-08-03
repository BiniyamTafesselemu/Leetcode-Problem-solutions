class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single=0
        double=0
        for i in nums:
            if i <=9:
                single+=i
            else:
                double+=i
        return single != double
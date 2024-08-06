class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_val=nums[-1]
        ans=0
        for i in range(k):
            ans+=max_val+i
        return ans
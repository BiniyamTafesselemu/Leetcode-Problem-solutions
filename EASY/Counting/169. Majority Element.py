class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        n=len(nums)
        ans=0
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for j in d:
            if d[j] > n/2:
                ans= j

        return ans
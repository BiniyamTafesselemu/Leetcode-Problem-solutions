class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        n=len(nums)
        ans=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for j in d:
            if d[j] > n/3:
                ans.append(j)

        return ans
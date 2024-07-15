class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        averages=[]
        l=0
        r=len(nums)-1
        while l<r:
            num=(nums[l] + nums[r])/2
            averages.append(num)
            l+=1
            r-=1
        return min(averages)
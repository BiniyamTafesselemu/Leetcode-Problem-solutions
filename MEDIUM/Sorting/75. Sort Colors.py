class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)):
            b=i+1
            while b < len(nums):
                if nums[b]<nums[i]:
                    nums[i],nums[b] = nums[b],nums[i]
                elif nums[i]==nums[b]:
                    nums[i+1],nums[b] = nums[b],nums[i+1]
                b+=1
        return nums



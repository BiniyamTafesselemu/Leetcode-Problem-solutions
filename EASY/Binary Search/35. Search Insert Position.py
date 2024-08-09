class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        mid_val=0
        while left <= right:
            mid=(left+right)//2
            mid_val=mid
            if nums[mid]==target:
                return mid
                break
            elif nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
        else:
            return left 
        
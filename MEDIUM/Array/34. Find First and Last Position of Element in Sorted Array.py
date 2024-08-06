from typing import List  

class Solution:  
    def searchRange(self, nums: List[int], target: int) -> List[int]:  
        def findLeftIndex(nums, target):  
            left, right = 0, len(nums) - 1  
            while left <= right:  
                mid = (left + right) // 2  
                if nums[mid] < target:  
                    left = mid + 1  
                else:  
                    right = mid - 1  
            return left  # This will be the leftmost index of target  

        def findRightIndex(nums, target):  
            left, right = 0, len(nums) - 1  
            while left <= right:  
                mid = (left + right) // 2  
                if nums[mid] <= target:  
                    left = mid + 1  
                else:  
                    right = mid - 1  
            return right  # This will be the rightmost index of target  

        left_index = findLeftIndex(nums, target)  
        right_index = findRightIndex(nums, target)  

        # Validate if the target is not found  
        if left_index <= right_index and left_index < len(nums) and nums[left_index] == target:  
            return [left_index, right_index]  
        else:  
            return [-1, -1]
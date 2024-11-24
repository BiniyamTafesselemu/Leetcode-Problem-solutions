class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0  # Pointer for the position of non-val elements

        for i in range(len(nums)):
            if nums[i] != val:  # Only consider elements that are not equal to val
                nums[l] = nums[i]  # Place it in the next position
                l += 1  # Move the pointer for non-val elements
        
        return l  # Return the count of non-val elements

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique_index = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index - 1]:
                nums[unique_index] = nums[i]
                unique_index += 1
        
        for j in range(unique_index, len(nums)):
            nums[j] = "_"
        
        return unique_index

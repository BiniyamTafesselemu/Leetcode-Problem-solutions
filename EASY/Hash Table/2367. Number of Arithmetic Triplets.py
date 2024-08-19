class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        num_set = set(nums)
        count=0
        for j in range(len(nums)):
            if nums[j]-diff in num_set and nums[j] + diff in num_set:
                count+=1
        return count
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        contains_duplicates = len(nums) != len(nums_set)
        return contains_duplicates
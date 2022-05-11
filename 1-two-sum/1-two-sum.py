class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = dict()
        
        for i, value in enumerate(nums):
            diff = target - value
            if diff in values:
                return [values[diff], i]
            
            values[value] = i
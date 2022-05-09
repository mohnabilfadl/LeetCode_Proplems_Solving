class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        max_curr = max_sub
        
        for i in range(1, len(nums)):

            max_curr = max(nums[i], max_curr + nums[i])
            max_sub = max(max_curr, max_sub)
            
        return max_sub
            
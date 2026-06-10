class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #     [  2   3   4   5   6]
        #     [  1   2   6  24 120]

        # nums = [2, 3, 4, 5, 6]

        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
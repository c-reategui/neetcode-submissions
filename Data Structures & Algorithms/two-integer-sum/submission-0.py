class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        # x + y = target
        # y = target - x
        for i, x in enumerate(nums):
            y = target - x
            if y in seen:
                return [seen[y], i]
            seen[x] = i
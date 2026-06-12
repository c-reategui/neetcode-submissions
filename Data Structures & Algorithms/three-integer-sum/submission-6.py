class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        n = len(nums)
        while i < n - 2:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            j, k = i + 1, n - 1
            while j < k:
                calc = nums[i] + nums[j] + nums[k]
                if calc < 0:
                    j += 1
                elif calc > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
            i += 1
        return res
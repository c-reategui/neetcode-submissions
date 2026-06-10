class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #     [  2   3   4   5   6]
        #     [  1   2   6  24 120 720] pre
        #     [720 360 120  30   6   1] post
        #     [360 240 180 144 120]
        # nums = [2, 3, 4, 5, 6]

        n = len(nums)
        pre = [1] * (n + 1)
        post = [1] * (n + 1)

        for i in range(1, n + 1):
            pre[i] = pre[i - 1] * nums[i - 1]
        
        for i in range(n - 1, -1, -1):
            post[i] = post[i + 1] * nums[i]
        
        ans = []
        for i in range(len(nums)):
            ans.append(pre[i] * post[i + 1])
        
        return ans

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d_counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in d_counter.items():
            buckets[value].append(key)

        ans = []
        for i in range(len(nums), -1, -1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

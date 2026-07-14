class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            hm[nums[i]] = hm.get(nums[i], 0) + 1
        for i, v in hm.items():
            freq[v].append(i)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
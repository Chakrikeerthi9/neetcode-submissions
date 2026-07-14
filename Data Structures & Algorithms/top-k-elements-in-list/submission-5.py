class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        count = [[] for i in range(len(nums)+1)]

        for i in nums:
            h[i] = h.get(i, 0) + 1
        for y,v in h.items():
            count[v].append(y)
        
        res = []
        for j in range(len(count) - 1, 0, -1):
            for l in count[j]:
                res.append(l)
                if len(res) == k:
                    return res

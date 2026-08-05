class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = defaultdict()
        for i, n in enumerate(nums):
            if (target - n) in hm.keys():
                if i > hm[target - n]:
                    return [hm[target - n], i]
                else:
                    return [i, hm[target - n]]
            hm[n] = i
        return []
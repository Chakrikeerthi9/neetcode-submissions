class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sample = {}
        li = []
        for i,n in enumerate(nums):
            sam = target - n
            if sam in sample:
                li += [sample[sam]]
                li += [i]
            sample[n] = i
        return li

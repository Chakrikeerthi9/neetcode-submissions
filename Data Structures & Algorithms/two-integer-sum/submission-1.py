class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sample = {}
        for i,n in enumerate(nums):
            sam = target - n
            if sam in sample:
                return [sample[sam],i]
            sample[n] = i

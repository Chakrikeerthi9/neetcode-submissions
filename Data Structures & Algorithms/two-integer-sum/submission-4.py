class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sam = {}
        for i,n in enumerate(nums):
            differ = target - n
            if differ in sam.keys():
                return [sam[differ],i]
            sam[n] = i
        return []

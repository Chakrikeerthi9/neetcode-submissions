class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sam = {}
        for i, n in enumerate(nums):
            if n in sam.keys():
                return True
            sam[n] = i
        return False
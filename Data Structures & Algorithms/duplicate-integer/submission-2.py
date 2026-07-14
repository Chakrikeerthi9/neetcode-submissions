class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sample = {}
        count = 0
        for i,n in enumerate(nums):
            if n in sample.values():
                count += 1
            else:
                sample[i] = n
        if count > 0:
            return True
        else:
            return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sample = {}
        count = 0
        for i,n in enumerate(nums):
            if n in sample.values():
                count += 1
                return True
            else:
                sample[i] = n
        return False
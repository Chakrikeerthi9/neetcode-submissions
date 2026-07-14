class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sample = set()
        for i in nums:
            if i in sample:
                return True
            sample.add(i)
        return False

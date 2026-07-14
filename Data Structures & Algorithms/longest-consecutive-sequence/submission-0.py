class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res, count = 0, 0
        for i in nums:
            j = i - 1
            while j in nums:
                count += 1
                j -= 1
            res = max(res, count + 1)
            count = 0
        return res
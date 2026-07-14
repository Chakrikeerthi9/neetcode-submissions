class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        res, count = 0, 0
        for i in nums:
            j = i - 1
            while j in nums:
                print(count,j)
                count += 1
                j -= 1
            res = max(res, count)
            count = 0
        return res + 1
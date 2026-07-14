class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        count = len(nums)
        while i < count:
            j = i + 1
            prod = 1
            while j < (i+count):
                prod *= nums[j % (count)]
                j += 1
            i += 1
            res.append(prod)
        return res
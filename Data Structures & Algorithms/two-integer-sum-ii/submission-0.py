class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a, b = 0, len(numbers) - 1
        while a < b:
            sums = numbers[a] + numbers[b]
            if sums > target :
                b -= 1
            elif sums < target :
                a += 1
            else:
                return [a + 1,b + 1]
        return []
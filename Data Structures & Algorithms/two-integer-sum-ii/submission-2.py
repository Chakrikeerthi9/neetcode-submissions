class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = {}
        for i, n in enumerate(numbers):
            if (target - n) in hm.keys():
                return [i+1, hm[target - n]+1] if i < hm[target - n] else [hm[target - n]+1, i+1]
            hm[n] = i
        print(hm)
        return []
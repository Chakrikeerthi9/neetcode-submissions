class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sam = [0] * 26
        for i in s:
            cal = (ord(i) - ord('a'))
            sam[cal] += 1
        ham = [0] * 26
        for j in t:
            sal = (ord(j) - ord('a'))
            ham[sal] += 1
        return True if sam == ham else False
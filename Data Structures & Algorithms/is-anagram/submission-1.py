class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sam1 = {}
        sam2 = {}
        for i, n in enumerate(s):
            sam1[n] = sam1.get(n,0) + 1
        for i, m in enumerate(t):
            sam2[m] = sam2.get(m,0) + 1
        if sam1 == sam2 :
            return True
        else:
            return False
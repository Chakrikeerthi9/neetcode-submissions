class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = {}
        for i in s:
            hm1[i] = hm1.get(i, 0) + 1
        
        hm2 = {}
        for j in t:
            hm2[j] = hm2.get(j, 0) + 1
        
        return hm1 == hm2
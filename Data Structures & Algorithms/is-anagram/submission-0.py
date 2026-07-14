class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            a1 = list(s)
            a2 = list(t)
            for i in a1:
                if i in a2:
                    a2.remove(i)
            if len(a2) == 0 :
                return True
        return False
        
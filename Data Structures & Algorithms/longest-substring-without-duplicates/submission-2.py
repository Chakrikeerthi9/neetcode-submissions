class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        r = 0
        res = 0
        for i in range(len(s)):
            if s[i] in hm:
                r = max(r, hm[s[i]] + 1)
            hm[s[i]] = i
            res = max(res, i - r + 1)
        return res
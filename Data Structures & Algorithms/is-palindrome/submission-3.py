class Solution:
    def isPalindrome(self, s: str) -> bool:
        sam = ""
        for i in s.lower():
            if i.isalnum():
                sam += i
        for j in range(len(sam)):
            k = (-1 - j)
            if sam[j] == sam[k]:
                continue
            else:
                return False
        return True
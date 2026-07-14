class Solution:
    def isPalindrome(self, s: str) -> bool:
        sam = ""
        for i in s.lower():
            if i.isalnum():
                sam += i
        if sam == sam[::-1]:
            return True
        else:
            return False
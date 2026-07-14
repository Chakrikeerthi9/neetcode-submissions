import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]','',s)
        l = len(s)
        a = 0
        b = l - 1
        while a <= b:
            if s[a].lower() == s[b].lower():
                a += 1
                b -= 1
            else:
                return False
        return True


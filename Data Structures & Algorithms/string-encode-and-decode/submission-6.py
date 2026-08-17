class Solution:

    def encode(self, strs: List[str]) -> str:
        wrd = ""
        for i in strs:
            wrd += str(len(i)) + "#" + i
        return wrd

    def decode(self, s: str) -> List[str]:
        res = []
        x = 0
        while x < len(s):
            y = x 
            while s[y] != "#":
                y += 1
            
            length = int(s[x:y])
            start = y + 1
            end = start + length
            
            res.append(s[start:end])

            x = end
        return res
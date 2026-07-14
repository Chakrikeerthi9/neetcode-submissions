class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            sm = [0] * 26
            for j in i:
                sm[ord(j) - ord('a')] += 1
            res[tuple(sm)].append(i)
        return list(res.values())

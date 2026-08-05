class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm : defaultdict[tuple,List[str]] = defaultdict(list)

        for word in strs:
            sorted_word = tuple(sorted(word))
            hm[sorted_word].append(word)
        return list(hm.values())
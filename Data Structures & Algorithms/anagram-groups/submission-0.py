from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_group = defaultdict(list)
        result = []

        for s in strs:
            sort_str = tuple(sorted(s))
            anagram_group[sort_str].append(s)

        for v in anagram_group.values():
            result.append(v)

        return result



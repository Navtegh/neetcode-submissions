from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for i in range(len(strs)):
            x= sorted(strs[i])
            d["".join(x)].append(strs[i])
        return list(d.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for st in strs:
            count = [0]*26
            for exa in st:
                count[ord(exa)-ord('a')]+=1
            key = tuple(count)
            group[key].append(st)

        return list(group.values())

            
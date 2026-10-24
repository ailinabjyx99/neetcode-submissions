class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for ch in s:
            d[ch] = d.get(ch,0)+1
        for ch in t:
            d[ch] = d.get(ch,0)-1

        for value in d.values():
            if value != 0:
                return False
        return True

            
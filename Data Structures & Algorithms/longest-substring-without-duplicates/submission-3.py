class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        length = 0
        for right, ch in enumerate(s):
            if ch in seen:
                left = max(left,seen[ch]+1)
            seen[ch] = right
            length = max(right-left+1,length)

        return length
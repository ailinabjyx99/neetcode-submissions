class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxcount = 0
        count = {}
        result = 0
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0)+1
            maxcount = max(count[s[right]],maxcount)
            while right-left+1-maxcount>k:
                count[s[left]] = count.get(s[left])-1
                left+=1
            result = max(right-left+1,result)

        return result
            
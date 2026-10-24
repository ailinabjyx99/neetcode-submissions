class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = {}
        for index,ch in enumerate(s1):
            seen[ch] = seen.get(ch,0)+1
        current = {}
        left = 0
        for right, ch in enumerate(s2):
            current[ch] = current.get(ch,0)+1
            if right-left+1>len(s1):
                left_ch = s2[left]
                current[left_ch]-=1
                if current[left_ch] == 0:
                    del current[left_ch]
                left+=1
            if current==seen: #字典之间可以直接用==比较
                return True
        return False




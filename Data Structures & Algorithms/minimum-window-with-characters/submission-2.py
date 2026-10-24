class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {} #t的字典
        required = 0 #t需要的总的字符数量
        window = {} #目前加进来的总的字符
        have = 0 #需要满足要求的字符种类数量
        left = 0
        minlength = float('inf')
        result = ""

        for ch in t: #把t转化成字典
            need[ch] = need.get(ch,0)+1
        
        required = len(need)
        for right in range(len(s)): #遍历s
            ch = s[right]
            window[ch] = window.get(ch,0)+1
            if ch in need and window[ch]==need[ch]: #当前字符满足要求了
                have+=1
            while have == required: #所有字符都满足要求了
                currentlength = right-left+1
                if currentlength<minlength:
                    minlength = currentlength
                    result = s[left:right+1]
                window[s[left]]-=1
                left_ch = s[left]
                left+=1
                if left_ch in need and window[left_ch]<need[left_ch]:
                    have-=1
                    continue
        return result
                        
             
        
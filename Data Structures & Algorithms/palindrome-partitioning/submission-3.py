class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def palinrome(s):
            left,right = 0,len(s)-1
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        
        def backtrack(checkpoint,path):
            if checkpoint==len(s):
                res.append(path[:])
                return
            for i in range(checkpoint,len(s)):
                if not palinrome(s[checkpoint:i+1]):
                    continue
                path.append(s[checkpoint:i+1])
                backtrack(i+1,path)
                path.pop()

        backtrack(0,[])
        return res
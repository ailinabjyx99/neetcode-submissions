class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def palindrome(s):
            left,right = 0,len(s)-1
            while left<right:
                if s[left]==s[right]:
                    left+=1
                    right-=1
                else:
                    return False
            return True
        
        def backtrack(path,cutpoint):
            if cutpoint==len(s):
                res.append(path[:])
                return

            for i in range(cutpoint,len(s)):
                substring = s[cutpoint:i+1]
                if palindrome(substring):
                    path.append(substring)
                    backtrack(path,i+1)
                    path.pop()

        backtrack([],0)
        return res


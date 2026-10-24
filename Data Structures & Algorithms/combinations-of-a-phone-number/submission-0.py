class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        according = {}
        according["2"]={"a","b","c"}
        according["3"]={"d","e","f"}
        according["4"]={"g","h","i"}
        according["5"]={"j","k","l"}
        according["6"]={"m","n","o"}
        according["7"]={"p","q","r","s"}
        according["8"]={"t","u","v"}
        according["9"]={"w","x","y","z"}

        def backtrack(currentpoint,current):
            if currentpoint==len(digits):
                res.append("".join(current))
                return
            for ch in according[digits[currentpoint]]:
                current.append(ch)
                backtrack(currentpoint+1,current)
                current.pop()
        backtrack(0,[])
        return res

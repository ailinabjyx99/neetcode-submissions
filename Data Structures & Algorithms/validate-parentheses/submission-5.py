class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)%2==1:
            return False

        for ch in s:
            if ch == '(':
                stack.append(')')
            elif ch == '[':
                stack.append(']')
            elif ch =='{':
                stack.append('}')
            else:
                if stack and stack.pop()==ch:
                    continue
                else:
                    return False
        if len(stack)!=0:
            return False
        return True
                
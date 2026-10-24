class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item not in '*/+-':
                stack.append(int(item))
            else:
                b = stack.pop()
                a = stack.pop()
                if item == '+':
                    stack.append(a+b)
                elif item == '-':
                    stack.append(a-b)
                elif item == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        return stack.pop()
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for item,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                prev = stack.pop()
                result[prev]=item-prev
            stack.append(item)
        return result

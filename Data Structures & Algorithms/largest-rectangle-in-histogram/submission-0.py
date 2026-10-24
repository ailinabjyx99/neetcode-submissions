class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = float('-inf')

        for index, height in enumerate(heights):
            start = index
            while stack and height<stack[-1][1]:
                i,h = stack.pop()
                maxarea = max(maxarea,(index-i)*h)
                start = i
            stack.append([start,height])

        for index, height in stack:
            maxarea = max(maxarea,height*(len(heights)-index))

        return maxarea
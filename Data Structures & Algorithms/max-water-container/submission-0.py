class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        maxarea = 0

        while left<right:
            length = right-left
            if heights[left]<heights[right]:
                area = length*heights[left]
                left+=1
            else:
                area = length*heights[right]
                right-=1
            maxarea = max(area,maxarea)
        return maxarea

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        

        while left<right:
            hour = 0
            mid = (right+left)//2
            for p in piles:
                hour += math.ceil(p/mid)
            if hour <= h:
                right = mid
            else:
                left = mid+1
        return left

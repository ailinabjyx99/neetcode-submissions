class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        low = float('inf')
        for index,price in enumerate(prices):
            low = min(low,price)
            result = max(result,price-low)
        return result



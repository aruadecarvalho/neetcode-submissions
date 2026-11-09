class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) == 0:
            return profit
        
        l = 0
        for r in range(len(prices)):
            if prices[r] - prices[l] < 0:
                l = r
            else:
                profit = max(profit, prices[r] - prices[l])

        return profit
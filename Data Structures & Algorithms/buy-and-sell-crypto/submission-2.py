class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Return the maximal amount of profit
        # The sell point must come after the buy point 
        if len(prices) == 0:
            return 0
        buy = prices[0]
        sell = prices[0]
        profit = 0

        for i, price in enumerate(prices, start = 1):
            if price < buy:
                buy = price
                sell = price
            if price > sell:
                sell = price
            
            profit = sell - buy if sell - buy > profit else profit

        return profit
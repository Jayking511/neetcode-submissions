class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0]
        for i in range(len(prices)):
            if i == len(prices)-1:
                continue
            if prices[i] > max(prices[i+1:]):
                continue
            else:
                profit.append(max(prices[i+1:]) - prices[i])
        return max(profit)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minCost=prices[0]
        for i in range(len(prices)):
            if (prices[i]-minCost >= profit):
                profit=prices[i]-minCost
            if (prices[i] < minCost):
                minCost=prices[i]
        return profit

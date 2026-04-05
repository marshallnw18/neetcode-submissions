class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # variable length window
        # find max difference between k[0] and k[1]?

        length = 0
        L = 0
        maxProfit = 0

        for R in range(1, len(prices)):
            if prices[R] < prices[L]:
                L = R
            else:
            # if diff prices[R] - prices[L] > maxProfit
                maxProfit = max(maxProfit, prices[R] - prices[L])
        
        return maxProfit


            
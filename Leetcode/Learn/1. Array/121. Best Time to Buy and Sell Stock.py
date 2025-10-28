class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Initialize left pointer at 0 and right pointer at 1
        Move right pointer till right < len(prices) using a while loop
        If prices[right] > prices[left]
          Then update the max_profit
        else
          Increment l = r
        Since it is a while loop, increment r by 1 at the end of the loop
        """
        
        l = 0  # buy day
        r = 1  # sell day
        max_profit = 0

        while r < len(prices):
        # if current sell price is greater than buy price → profit 
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                # found a cheaper price: update buy day
                l = r
            r = r + 1

        return max_profit

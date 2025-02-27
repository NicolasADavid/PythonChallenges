"""
You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.

A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.

Return the number of smooth descent periods.
"""

class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        last = None
        descent_periods = 0
        running = 0

        for price in prices:

            # Add the one day period
            descent_periods += 1

            if last:
                if price == last - 1:
                    # Add every day of the smooth descent period
                    running += 1
                else:
                    running = 0
                    
            descent_periods += running
            last = price

        return descent_periods
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        want to buy low, sell high
        maximize the profit

        profit variable
        low variable


        iterate through prices
            
        '''

        profit = 0
        low = prices[0]

        for price in prices:
            if price - low > profit:
                profit = price - low
            low = min(low, price)
        return profit
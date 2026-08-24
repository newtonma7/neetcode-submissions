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

        for cost in prices:
            temp = cost - low
            if profit < temp:
                profit = temp
            low = min(low,cost)
        return profit
        
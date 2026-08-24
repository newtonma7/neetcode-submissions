class Solution {
    public int maxProfit(int[] prices) {
        /*
            buy low sell high
        */
        int min = prices[0];
        int profit = 0;

        for(int i = 0; i < prices.length; i++){
            if(prices[i] < min){
                min = prices[i];
            }
            int money = prices[i] - min;
            if(money > profit){
                profit = money;
            }
        }
        return profit;

    }
}

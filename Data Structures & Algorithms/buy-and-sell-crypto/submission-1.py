class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # record the min 
        # increment ptr 
        # if num > min, calculate profit and continue 
        # if num < min, make it new min 
        msf = prices[0]
        profit = 0 
        for num in prices: 
            if num < msf: 
                msf = num 
            profit = max(profit, num-msf)
        return profit 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,profit=0,0
        right=1
        while right<len(prices):
            if prices[right]-prices[left]<0:
                left=right
                right+=1
            else:
                profit=max(profit,prices[right]-prices[left])
                right+=1
        return profit

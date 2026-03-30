class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        min_price = 101
        for i in prices:
            if i < min_price:
                min_price =i
            maxP = max(maxP, i- min_price)
        
        return maxP
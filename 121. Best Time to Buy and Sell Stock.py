class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=[]
        min_price=prices[0]
        for i in range(1,len(prices)):
            if prices[i]>min_price:
                res.append(prices[i]-min_price)
            else:
                min_price=prices[i]
        if res:
            return max(res)
        else:
            return 0
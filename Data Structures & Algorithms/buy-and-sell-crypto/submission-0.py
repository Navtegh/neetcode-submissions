class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=0
        maxp=0
        minv=prices[l]
        while r<len(prices):
            if prices[r]>prices[l]:
                maxp=max(maxp,prices[r]-prices[l])
            if minv>prices[r]:
                minv=prices[r]
                l=r
            r=r+1
        return maxp
        
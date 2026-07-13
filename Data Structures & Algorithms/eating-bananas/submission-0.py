import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        res=0
        while low<=high:
            mid=int(low+(high-low)/2)
            total=0
            for i in range(len(piles)):
                total+=math.ceil(piles[i]/mid)
            if total<=h:
                res=mid
                high=mid-1
                mid=int(low+(high-low)/2)
            else:
                low=mid+1
                mid=int(low+(high-low)/2)
        return res
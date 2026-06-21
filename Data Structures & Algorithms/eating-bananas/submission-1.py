import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high=1,max(piles)
        res=high
        while low<=high:
            k=(low+high)//2
            temp=0
            for i in piles:
                temp+=math.ceil(i/k)
            if temp<=h:
                high=k-1
                res=min(res,k)
            else:
                low=k+1

        return res
            

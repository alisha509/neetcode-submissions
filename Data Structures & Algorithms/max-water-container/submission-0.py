class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        for left in range(len(heights)):
            right=len(heights)-1
            while left<right:
                if heights[left]>heights[right]:
                    area=max(area,heights[right]*(right-left))
                else:
                    area=max(area,heights[left]*(right-left))
                right-=1
        return area    

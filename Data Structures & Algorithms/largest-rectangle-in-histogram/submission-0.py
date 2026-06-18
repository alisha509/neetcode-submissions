class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=0
        for i, val in enumerate(heights):
            start=i
            while stack and stack[-1][1]>val:
                index, height=stack.pop()
                max_area=max(max_area, height*(i-index))
                start=index
            stack.append((start,val))
        for i, h in stack:
            max_area=max(max_area,h*(len(heights)-i))
        return max_area
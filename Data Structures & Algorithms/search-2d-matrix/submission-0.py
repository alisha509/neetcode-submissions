class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col= len(matrix), len(matrix[0])
        low,high=0,row-1
        while low<=high:
            mid=(low+high)//2
            if matrix[mid][-1]<target:
                low=mid+1
            elif matrix[mid][0]>target:
                high=mid-1
            else:
                break
        if not (low<=high):
            return False
        mid=(low+high)//2
        l,r=0, col-1
        while l<=r:
            m=(l+r)//2
            if target>matrix[mid][m]:
                l=m+1
            elif target<matrix[mid][m]:
                r=m-1
            else:
                return True
        return False


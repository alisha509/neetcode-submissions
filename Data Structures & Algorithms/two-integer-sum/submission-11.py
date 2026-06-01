class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new={}
        for i,x in enumerate(nums):
            diff=target-x
            if diff in new:
                return [new[diff],i]
            new[x]=i
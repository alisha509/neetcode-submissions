class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new={}
        for i,num in enumerate(nums):
            j=target-num
            if j in new:
                return [new[j],i]
            new[num]=i
        
    
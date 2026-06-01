class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        empty_set=set(nums)
        longest=0
        for i in empty_set:
            if i-1 not in empty_set:
                start=1
                while i+start in empty_set:
                    start+=1
                longest = max(longest,start)
        return longest
        
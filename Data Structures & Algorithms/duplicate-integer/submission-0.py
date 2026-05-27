class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test = {}
        for i in nums:
            if i not in test:
                test[i]=1
            else:
                return True
        return False


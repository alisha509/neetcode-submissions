from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1=defaultdict(int)
        count2=defaultdict(int)
        left=0
        for right in range(len(s1)):
            count1[s1[right]]+=1
        for right in range(len(s2)):
            count2[s2[right]]+=1
            if len(s1)<right-left+1:
                count2[s2[left]]-=1
                if count2[s2[left]] == 0:
                    del count2[s2[left]]
                left+=1

            if len(s1)==right-left+1:
                if count1==count2:
                    return True
        return False
               
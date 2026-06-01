class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new={}
        new1={}
        for i in s:
            if i not in new:
                new[i]=1
            else:
                new[i]+=1
        for i in t:
            if i not in new1:
                new1[i]=1
            else:
                new1[i]+=1
        return(new==new1)
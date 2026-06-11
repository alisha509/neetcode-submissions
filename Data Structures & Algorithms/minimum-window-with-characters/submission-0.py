from collections import defaultdict
class Solution:
        def minWindow(self, s: str, t: str) -> str:
            window=defaultdict(int)
            countT=defaultdict(int)
            for c in t:
                countT[c]+=1
            have=0
            need=len(countT)
            res, res_len=[-1,-1], float("infinity")
            left=0
            for right in range(len(s)):
                window[s[right]]+=1
                if s[right] in countT and window[s[right]]==countT[s[right]]:
                    have+=1
                while have==need:
                    if (right-left+1)<res_len:
                        res=[left,right]
                        res_len=right-left+1
                    window[s[left]]-=1
                    if s[left] in countT and window[s[left]]<countT[s[left]]:
                        have-=1
                    left+=1
            left, right=res
            return s[left:right+1] if res_len != float("infinity") else ""

            
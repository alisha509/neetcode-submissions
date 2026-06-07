class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        max_f=0
        max_len=0
        freq=[0]*26
        for right in range(len(s)):
            freq[ord(s[right])-ord('A')]+=1
            max_f=max(max_f,freq[ord(s[right])-ord('A')])
            if (right-left+1)-max_f>k:
                freq[ord(s[left])-ord('A')]-=1
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len
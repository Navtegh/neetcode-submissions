class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L=0
        R=0
        x=set()
        # x.add(s[0])
        maxl=0
        while R<=len(s)-1:
            if s[R] not in x:
                x.add(s[R])
                R+=1
            else:
                x.remove(s[L])
                L+=1
            print(x)
            maxl=max(R-L, maxl)

        return maxl
                


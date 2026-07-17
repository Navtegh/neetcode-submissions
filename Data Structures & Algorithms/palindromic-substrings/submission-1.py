class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        if n==1:
            return 1
        l=0
        r=1
        maxstr=list(s)
        while l<r and r<n:
            rev=s[l:r+1]
            if s[l:r+1]==rev[::-1]:
                maxstr.append(s[l:r+1])
            if r<n-1:
                r=r+1
            elif r==n-1:
                l=l+1
                r=l+1
        return len(maxstr)

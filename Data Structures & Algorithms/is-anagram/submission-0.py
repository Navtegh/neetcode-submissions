class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        else:
            d={}
            x={}
            for i in range(len(s)):
                if s[i] in d:
                    d[s[i]]+=1
                else:
                    d[s[i]]=1
                if t[i] in x:
                    x[t[i]]+=1
                else:
                    x[t[i]]=1
            if x==d:
                return True
            else:
                return False
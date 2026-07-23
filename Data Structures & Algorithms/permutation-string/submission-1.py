class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        c1=[0]*26
        c2=[0]*26
        for i in range(len(s1)):
            n=ord(s1[i])-ord("a")
            c1[n]+=1
        prev=0
        for i in range(len(s2)):
            if i<len(s1):
                n=ord(s2[i])-ord("a")
                c2[n]+=1

            else:
                prev=ord(s2[i-len(s1)]) -ord("a")
                n=ord(s2[i])-ord("a")
                c2[prev]-=1
                c2[n]+=1
            if c1==c2:
                return True


        return False

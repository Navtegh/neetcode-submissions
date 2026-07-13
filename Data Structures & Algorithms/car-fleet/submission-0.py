class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pt=[]
        res=1
        for i in range(len(position)):
            d=target-position[i]
            pt.append((position[i],d/speed[i]))
        pt.sort(key=lambda pair:pair[0])
        p,maxt=pt.pop()
        while pt:
            p,t=pt.pop()
            if t<=maxt:
                continue
            else:
                maxt=t
                res=res+1
        return res
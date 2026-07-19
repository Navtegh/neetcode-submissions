class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kmindis=[]
        res=[]
        for x,y in points:
            dist=-1*(x**2 + y**2)
            heapq.heappush(kmindis,[dist,x,y])
            if len(kmindis)>k:
                heapq.heappop(kmindis)

        n=len(kmindis)
        for i in range(n):
            dist,x,y=heapq.heappop(kmindis)
            res.append([x,y])
        return res


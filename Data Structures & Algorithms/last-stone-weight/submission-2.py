class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minstones=[-x for x in stones]
        heapq.heapify(minstones)
        while(len(minstones)>1):
            x=heapq.heappop(minstones)
            y=heapq.heappop(minstones)
            if y>x:
                heapq.heappush(minstones,x-y)

        minstones.append(0)
        return abs(minstones[0])


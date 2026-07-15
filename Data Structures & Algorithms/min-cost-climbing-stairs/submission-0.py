class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        total=[-1]*n
        def dfs(i):
            if i>=n:
                return 0
            if total[i]!=-1:
                return total[i]
            total[i]=cost[i]+ min(dfs(i + 1),dfs(i + 2))
            return total[i]
        return min(dfs(0), dfs(1))

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROWS=len(grid)
        COLS=len(grid[0])
        area=0
        def dfs(grid,r,c):
            nonlocal area
            if min(r,c)<0 or r==ROWS or c==COLS or grid[r][c]==0:
                return None
            else:
                grid[r][c]=0
                area+=1
            dfs(grid,r,c+1)
            dfs(grid,r,c-1)
            dfs(grid,r-1,c)
            dfs(grid,r+1,c)
            return area


        maxarea=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    continue
                elif grid[r][c]==1:
                    area=0
                    maxarea=max(maxarea,dfs(grid,r,c))
        return maxarea
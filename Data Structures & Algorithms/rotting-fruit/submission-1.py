class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))

        mins = -1

        def addCell(r, c):
            if (
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                grid[r][c] != 1
            ):
                return

            grid[r][c] = 2
            q.append((r, c))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)

            mins += 1

        for row in grid:
            if 1 in row:
                return -1

        return max(mins, 0)
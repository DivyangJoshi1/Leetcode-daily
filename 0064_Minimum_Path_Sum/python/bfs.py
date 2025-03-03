from heapq import heappop, heappush

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pq = [(grid[0][0], 0, 0)]
        directions = [(1, 0), (0, 1)]
        visited = set()

        while pq:
            cost, x, y = heappop(pq)
            if (x, y) in visited:
                continue
            visited.add((x, y))

            if x == m - 1 and y == n - 1:
                return cost

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    heappush(pq, (cost + grid[nx][ny], nx, ny))

        return -1  # Should never reach here

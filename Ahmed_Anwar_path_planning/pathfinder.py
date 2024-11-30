from typing import List, Optional, Set, Tuple
from grid import Grid

Position = Tuple[int, int]


class PathFinder:
    def __init__(self, grid: Grid, start: Position, goal: Position):
        self.grid = grid
        self.start = start
        self.goal = goal

    def compute_shortest_path(self) -> float:
        """Compute the shortest path using dynamic programming."""
        dp = self.grid.dp
        grid_size = self.grid.grid_size

        # Forward DP Pass
        for x in range(grid_size):
            for y in range(grid_size):
                if not self.grid.is_valid_cell(x, y):
                    continue
                if x > 0:  # From above
                    dp[x][y] = min(dp[x][y], dp[x - 1][y] + 1)
                if y > 0:  # From left
                    dp[x][y] = min(dp[x][y], dp[x][y - 1] + 1)

        # Backward DP Pass
        for x in range(grid_size - 1, -1, -1):
            for y in range(grid_size - 1, -1, -1):
                if not self.grid.is_valid_cell(x, y):
                    continue
                if x < grid_size - 1:  # From below
                    dp[x][y] = min(dp[x][y], dp[x + 1][y] + 1)
                if y < grid_size - 1:  # From right
                    dp[x][y] = min(dp[x][y], dp[x][y + 1] + 1)

        return dp[self.goal[0]][self.goal[1]]

    def reconstruct_path(self) -> Optional[List[Position]]:
        """Reconstruct the shortest path from start to goal."""
        dp = self.grid.dp
        if dp[self.goal[0]][self.goal[1]] == float("inf"):
            return None

        path = []
        current = self.goal
        path.append(current)

        while current != self.start:
            x, y = current
            neighbors = [
                (x - 1, y),
                (x + 1, y),
                (x, y - 1),
                (x, y + 1),
            ]
            min_cost = float("inf")
            next_cell = None

            for nx, ny in neighbors:
                if self.grid.is_valid_cell(nx, ny) and dp[nx][ny] < min_cost:
                    min_cost = dp[nx][ny]
                    next_cell = (nx, ny)

            path.append(next_cell)
            current = next_cell

        return path[::-1]  # Reverse to get path from start to goal

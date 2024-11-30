from typing import List, Set, Tuple

Position = Tuple[int, int]
Grid = List[List[float]]


class Grid:
    def __init__(self, grid_size: int, obstacles: Set[Position]):
        self.grid_size = grid_size
        self.obstacles = obstacles
        self.dp = self._initialize_grid()

    def _initialize_grid(self) -> Grid:
        """Initialize the grid with infinity and mark obstacles."""
        dp = [[float("inf")] * self.grid_size for _ in range(self.grid_size)]
        for x, y in self.obstacles:
            dp[x][y] = float("inf")  # Obstacles
        return dp

    def set_cost(self, x: int, y: int, cost: float) -> None:
        """Set the cost for a specific cell."""
        self.dp[x][y] = cost

    def get_cost(self, x: int, y: int) -> float:
        """Get the cost of a specific cell."""
        return self.dp[x][y]

    def is_valid_cell(self, x: int, y: int) -> bool:
        """Check if a cell is within bounds and not an obstacle."""
        return (
            0 <= x < self.grid_size
            and 0 <= y < self.grid_size
            and (x, y) not in self.obstacles
        )

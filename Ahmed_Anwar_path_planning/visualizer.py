import matplotlib.pyplot as plt
from typing import List, Optional, Set, Tuple

Position = Tuple[int, int]


class Visualizer:
    def __init__(
        self, grid_size: int, start: Position, goal: Position, obstacles: Set[Position]
    ):
        self.grid_size = grid_size
        self.start = start
        self.goal = goal
        self.obstacles = obstacles

    def visualize(self, path: Optional[List[Position]]) -> None:
        """Visualize the grid, obstacles, and path."""
        fig, ax = plt.subplots()
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                if (x, y) == self.start:
                    ax.text(
                        y,
                        self.grid_size - x - 1,
                        "S",
                        ha="center",
                        va="center",
                        color="blue",
                    )
                elif (x, y) == self.goal:
                    ax.text(
                        y,
                        self.grid_size - x - 1,
                        "G",
                        ha="center",
                        va="center",
                        color="green",
                    )
                elif (x, y) in self.obstacles:
                    ax.add_patch(
                        plt.Rectangle((y, self.grid_size - x - 1), 1, 1, color="red")
                    )
                else:
                    ax.add_patch(
                        plt.Rectangle(
                            (y, self.grid_size - x - 1),
                            1,
                            1,
                            edgecolor="black",
                            fill=False,
                        )
                    )

        if path:
            for x, y in path:
                ax.add_patch(
                    plt.Circle(
                        (y + 0.5, self.grid_size - x - 1 + 0.5), 0.3, color="yellow"
                    )
                )

        plt.xlim(0, self.grid_size)
        plt.ylim(0, self.grid_size)
        ax.set_aspect("equal")
        plt.grid(True)
        plt.show()

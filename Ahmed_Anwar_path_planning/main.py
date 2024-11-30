from typing import Set, Tuple
from grid import Grid
from pathfinder import PathFinder
from visualizer import Visualizer

Position = Tuple[int, int]


def main():
    grid_size = 5
    start: Position = (0, 1)
    goal: Position = (4, 4)
    obstacles: Set[Position] = {(2, 2), (2, 3), (3, 2), (3, 3)}

    # Initialize grid and pathfinder
    grid = Grid(grid_size, obstacles)
    grid.set_cost(start[0], start[1], 0)  # Set start position cost to 0
    pathfinder = PathFinder(grid, start, goal)

    # Compute shortest path
    shortest_distance = pathfinder.compute_shortest_path()
    path = pathfinder.reconstruct_path()

    # Output results
    print("Shortest Distance:", shortest_distance)
    print("Path:", path)

    # Visualize the solution
    visualizer = Visualizer(grid_size, start, goal, obstacles)
    visualizer.visualize(path)


if __name__ == "__main__":
    main()

import heapq
import random

# Directions for movement (up, down, left, right)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Manhattan distance heuristic
def manhattan_heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Greedy Best-First Search (GBFS)
def greedy_best_first_search(grid, start, end):
    open_list = []
    heapq.heappush(open_list, (manhattan_heuristic(start, end), start))  # (h, node)
    came_from = {}  # To reconstruct the path

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for direction in DIRECTIONS:
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                heapq.heappush(open_list, (manhattan_heuristic(neighbor, end), neighbor))
                came_from[neighbor] = current

    return None  # No path found

# Function to generate a random grid with obstacles
def generate_grid(size, num_obstacles):
    grid = [[0 for _ in range(size)] for _ in range(size)]
    obstacles = 0
    while obstacles < num_obstacles:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        if grid[x][y] == 0:  # Make sure it's empty
            grid[x][y] = 1  # Place obstacle
            obstacles += 1
    return grid

# Main function to run the GBFS algorithm
def run_gbfs_algorithm(grid_size, num_obstacles, start, end):
    grid = generate_grid(grid_size, num_obstacles)
    
    print(f"Running Greedy Best-First Search (GBFS)...")
    gbfs_path = greedy_best_first_search(grid, start, end)
    
    if gbfs_path:
        print("GBFS Path found:", gbfs_path)
    else:
        print("No path found using GBFS.")

# Example grid size (70x70 grid), obstacles (10), start and end points
grid_size = 70  # 70x70 grid (approx 5000 nodes)
num_obstacles = 10
start = (0, 0)
end = (69, 69)

run_gbfs_algorithm(grid_size, num_obstacles, start, end)

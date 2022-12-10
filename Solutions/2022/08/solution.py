"""Solution code"""
import pathlib
import sys


def parse(puzzle_input: str):
    """Parse input."""
    puzzle_input = puzzle_input.strip()
    grid: list[list[int]] = []
    for line in puzzle_input.splitlines():
        trees: list[int] = []
        for character in line:
            trees.append(int(character))
        grid.append(trees)
    return grid


def dfs_visible(grid: list[list[int]], row_index: int, col_index: int) -> bool:
    """Returns true if the tree is visible from the outside of the grid."""
    num_rows = len(grid)
    num_cols = len(grid[row_index])
    current_tree = grid[row_index][col_index]
    # Check if visible from top
    i = row_index
    while -1 < i:
        i -= 1
        if i < 0:
            return True
        if grid[i][col_index] >= current_tree:
            break
    # Check if visible from right
    i = col_index
    while i < num_cols:
        i += 1
        if i >= num_cols:
            return True
        if grid[row_index][i] >= current_tree:
            break
    # Check if visible from bottom
    i = row_index
    while i < num_rows:
        i += 1
        if i >= num_rows:
            return True
        if grid[i][col_index] >= current_tree:
            break
    # Check if visible from left
    i = col_index
    while -1 < i:
        i -= 1
        if i < 0:
            return True
        if grid[row_index][i] >= current_tree:
            break
    # Not visible
    return False


def part1(data: list[list[int]]):
    """Solve part 1."""
    # A tree is visible if we can get a bound of the grid without being blocked
    visible_trees = 0
    for row_index, row in enumerate(data):
        for col_index, _ in enumerate(row):
            if dfs_visible(data, row_index, col_index):
                visible_trees += 1
    return visible_trees


def dfs_scenic_score(grid: list[list[int]], row_index: int, col_index: int) -> int:
    """Returns the scenic score of a particular tree."""
    num_rows = len(grid)
    num_cols = len(grid[row_index])
    current_tree = grid[row_index][col_index]
    # Check score from top
    viewing_distance_top = 0
    for i in range(row_index - 1, -1, -1):
        viewing_distance_top += 1
        if grid[i][col_index] >= current_tree:
            break
    # Check score from right
    viewing_distance_right = 0
    for i in range(col_index + 1, num_cols):
        viewing_distance_right += 1
        if grid[row_index][i] >= current_tree:
            break
    # Check score from bottom
    viewing_distance_bottom = 0
    for i in range(row_index + 1, num_rows):
        viewing_distance_bottom += 1
        if grid[i][col_index] >= current_tree:
            break
    # Check score from left
    viewing_distance_left = 0
    for i in range(col_index - 1, -1, -1):
        viewing_distance_left += 1
        if grid[row_index][i] >= current_tree:
            break
    # Return scenic score
    return (
        viewing_distance_top
        * viewing_distance_right
        * viewing_distance_bottom
        * viewing_distance_left
    )


def part2(data: list[list[int]]):
    """Solve part 2."""
    highest_scenic_score = 0
    for row_index, row in enumerate(data):
        for col_index, _ in enumerate(row):
            scenic_score = dfs_scenic_score(data, row_index, col_index)
            highest_scenic_score = max(scenic_score, highest_scenic_score)
    return highest_scenic_score


def solve(puzzle_input: str):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    data = parse(puzzle_input)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        input_string = pathlib.Path(path).read_text("utf-8")
        solutions = solve(input_string)
        print("\n".join(str(solution) for solution in solutions))

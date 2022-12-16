"""Solution code"""
import pathlib
import sys
import math


def parse(puzzle_input: str):
    """Parse input."""
    puzzle_input = puzzle_input.strip()
    data: list[list[str]] = []

    for line in puzzle_input.splitlines():
        row: list[str] = []
        for character in line:
            row.append(character)
        data.append(row)

    return data


def is_within_elevation(a: str, b: str) -> bool:
    """Returns whether or not b is within climbing distance of a."""
    if a == "S":
        a = "a"
    if b == "E":
        b = "z"
    return 0 <= ord(b) - ord(a) <= 1


def get_visitable_neighbors(
    a: tuple[int, int], data: list[list[str]]
) -> list[tuple[int, int]]:
    """Returns visitable neighbor locations."""
    neighbors: list[tuple[int, int]] = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for direction in directions:
        b = (a[0] + direction[0], a[1] + direction[1])

        if b[0] < 0 or b[0] > len(data):
            continue
        if b[1] < 0 or b[1] > len(data):
            continue

        a_value = data[a[0]][a[1]]
        if a_value == "S":
            a_value = "a"
        b_value = data[b[0]][b[1]]
        if b_value == "E":
            b_value = "z"
        if 0 <= ord(b_value) - ord(a_value) <= 1:
            neighbors.append(b)
    return neighbors


def dfs(
    location: tuple[int, int],
    data: list[list[str]],
    visited: set[tuple[int, int]],
    path_length: int,
):
    visited.add(location)

    if data[location[0]][location[1]] == "E":
        return path_length

    # Get visitable neighbors
    neighbors = get_visitable_neighbors(location, data)
    if len(neighbors) == 0:
        return int(math.inf)

    path_lengths: list[int] = []
    for neighbor in neighbors:
        path_lengths.append(dfs(neighbor, data, visited, path_length + 1))

    return min(path_lengths)


def part1(data: list[list[str]]):
    """Solve part 1.

    Key idea: shortest path. Should used Dijkstra's or A*.
    """
    # Find the start location
    start_location: tuple[int, int] = (-1, -1)
    for row_i, row in enumerate(data):
        for col_i, neighbor_elevation in enumerate(row):
            if neighbor_elevation == "S":
                start_location = (row_i, col_i)
                break

    # Get visitable neighbors
    neighbors = get_visitable_neighbors(start_location, data)

    # Do DFS starting at each neighbor location
    path_lengths: list[int] = []
    for location in neighbors:
        path_lengths.append(dfs(location, data, set([start_location]), 1))

    return min(path_lengths)


def part2(data):
    """Solve part 2."""
    return 0


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

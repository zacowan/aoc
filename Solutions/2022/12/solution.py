"""Solution code"""
import pathlib
import sys
import math
from collections import defaultdict


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


def get_visitable_neighbors(
    node: tuple[int, int], graph: list[list[str]]
) -> list[tuple[int, int]]:
    """Returns visitable neighbor locations."""
    neighbors: list[tuple[int, int]] = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for direction in directions:
        neighbor = (node[0] + direction[0], node[1] + direction[1])

        if neighbor[0] < 0 or neighbor[0] >= len(graph):
            continue
        if neighbor[1] < 0 or neighbor[1] >= len(graph[0]):
            continue

        a_value = graph[node[0]][node[1]]
        if a_value == "S":
            a_value = "a"
        b_value = graph[neighbor[0]][neighbor[1]]
        if b_value == "E":
            b_value = "z"
        if 0 <= ord(b_value) - ord(a_value) <= 1:
            neighbors.append(neighbor)
    return neighbors


def get_elevation_diff(
    a: tuple[int, int], b: tuple[int, int], graph: list[list[str]]
) -> int:
    val_a = ord(graph[a[0]][a[1]])
    val_b = ord(graph[b[0]][b[1]])
    diff = val_b - val_a

    if diff < 0:
        return 0

    return diff


def part1(data: list[list[str]]):
    """Solve part 1.

    Key idea: shortest path. Should used Dijkstra's or A*.
    """
    # Find the start location and get all nodes
    unvisited: list[tuple[int, int]] = []
    start_location: tuple[int, int] = (-1, -1)
    end_location: tuple[int, int] = (-1, -1)

    for row_i, row in enumerate(data):
        for col_i, elevation in enumerate(row):
            unvisited.append((row_i, col_i))
            if elevation == "S":
                start_location = (row_i, col_i)
            elif elevation == "E":
                end_location = (row_i, col_i)

    shortest_path = defaultdict(lambda: math.inf)
    previous = {}
    shortest_path[start_location] = 0

    while unvisited:
        min_node = unvisited[0]
        min_i = 0
        for i, node in enumerate(unvisited):
            if shortest_path[node] < shortest_path[min_node]:
                min_node = node
                min_i = i

        neighbors = get_visitable_neighbors(min_node, data)
        for neighbor in neighbors:
            cost = shortest_path[min_node] + get_elevation_diff(
                min_node, neighbor, data
            )
            if cost < shortest_path[neighbor]:
                shortest_path[neighbor] = cost
                previous[neighbor] = min_node

        unvisited.pop(min_i)

    return shortest_path[end_location]


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

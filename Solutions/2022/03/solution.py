"""Solution code"""
import pathlib
import sys


def parse(puzzle_input: str):
    """Parse input."""
    rucksacks: list[str] = []
    for line in puzzle_input.splitlines():
        if line:
            rucksacks.append(line)
    return rucksacks


def compute_sum_priorities(item_types: list[str]):
    """Return the computed sum of the priorities of each item type."""
    res = 0
    for t in item_types:
        if ord("a") <= ord(t) <= ord("z"):
            # Lowercase
            res += ord(t) - ord("a") + 1
        else:
            # Uppercase
            res += ord(t) - ord("A") + 27
    return res


def part1(data: list[str]):
    """Solve part 1."""
    item_types: list[str] = []
    # For each list of contents
    for contents in data:
        # Split the contents into first and second compartments
        center = len(contents) // 2
        first = set(list(contents[0:center]))
        second = set(list(contents[center:]))
        # Store the common content
        item_types.append((first & second).pop())
    # Return the sum of priorities
    return compute_sum_priorities(item_types)


def part2(data: list[str]):
    """Solve part 2."""
    item_types: list[str] = []
    # Split into groups of 3 rucksacks
    current_group: set[str] = set()
    for i, contents in enumerate(data):
        if i % 3 == 0:
            if len(current_group) != 0:
                item_types.append(current_group.pop())
            current_group = set(list(contents))
        else:
            current_group = current_group & set(list(contents))
    if len(current_group) != 0:
        item_types.append(current_group.pop())
    # Return the sum of priorities
    return compute_sum_priorities(item_types)


def solve(puzzle_input: str):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        input_string = pathlib.Path(path).read_text("utf-8").strip()
        solutions = solve(input_string)
        print("\n".join(str(solution) for solution in solutions))

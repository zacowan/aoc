"""Solution code"""
import pathlib
import sys
from collections import deque


def parse(puzzle_input: str):
    """Parse input."""
    puzzle_input = puzzle_input.strip()
    return puzzle_input


def part1(data: str):
    """Solve part 1."""
    characters = deque()
    result = -1
    for i, c in enumerate(data):
        # Add characters to queue
        characters.append(c)
        # Check if there are 4 unique characters
        if i >= 3:
            if len(set(characters)) == 4:
                result = i + 1
                break
            else:
                characters.popleft()
    return result


def part2(data):
    """Solve part 2."""
    characters = deque()
    result = -1
    for i, c in enumerate(data):
        # Add characters to queue
        characters.append(c)
        # Check if there are 4 unique characters
        if i >= 13:
            if len(set(characters)) == 14:
                result = i + 1
                break
            else:
                characters.popleft()
    return result


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

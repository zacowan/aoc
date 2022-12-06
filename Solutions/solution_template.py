"""Solution code"""
import pathlib
import sys


def parse(puzzle_input: str):
    """Parse input."""
    return 0


def part1(data):
    """Solve part 1."""
    return 0


def part2(data):
    """Solve part 2."""
    return 0


def solve(puzzle_input: str):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        input_string = pathlib.Path(path).read_text("utf-8")
        solutions = solve(input_string)
        print("\n".join(str(solution) for solution in solutions))

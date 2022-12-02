"""Solution code"""
import pathlib
import sys
from heapq import heappop, heappush, heapify


def parse(puzzle_input: str):
    """Parse input."""
    calories = []  # calories each elf holds, max-heap
    current_calories = 0  # calories for the current elf
    heapify(calories)
    for data in puzzle_input.splitlines():
        if data:
            amount_calories = int(data)
            current_calories += amount_calories
        else:
            heappush(calories, current_calories * -1)
            current_calories = 0
    return calories


def part1(data: list[int]):
    """Solve part 1."""
    # Return the max amount of calories being carried
    max_calories = heappop(data)
    heappush(data, max_calories)
    return max_calories * -1


def part2(data):
    """Solve part 2."""
    # Return the sum of the top 3 elves carrying calories
    top_3 = []
    for _ in range(3):
        top_3.append(heappop(data))
    return sum(top_3) * -1


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

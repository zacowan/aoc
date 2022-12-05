"""Solution code"""
import pathlib
import sys


class SectionRange:
    """Wrapper for the section ranges covered."""

    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end


def parse(puzzle_input: str):
    """Parse input."""
    data: list[tuple[SectionRange, SectionRange]] = []
    for line in puzzle_input.splitlines():
        if line:
            ranges = line.split(",")
            first, second = ranges[0], ranges[1]
            first_split, second_split = first.split("-"), second.split("-")
            first_start, first_end = int(first_split[0]), int(first_split[1])
            second_start, second_end = int(second_split[0]), int(second_split[1])
            first_range, second_range = SectionRange(
                first_start, first_end
            ), SectionRange(second_start, second_end)
            data.append((first_range, second_range))
    return data


def part1(data: list[tuple[SectionRange, SectionRange]]):
    """Solve part 1."""
    overlap_count = 0
    for pair in data:
        (first, second) = pair
        # First contained within second
        if second.start <= first.start and first.end <= second.end:
            overlap_count += 1
        # Second contained within first
        elif first.start <= second.start and second.end <= first.end:
            overlap_count += 1
    return overlap_count


def part2(data: list[tuple[SectionRange, SectionRange]]):
    """Solve part 2."""
    overlap_count = 0
    for pair in data:
        (first, second) = pair
        # First overlaps partially with second
        if (
            second.start <= first.start <= second.end
            or second.start <= first.end <= second.end
        ):
            overlap_count += 1
        # Second overlaps partially with first
        elif (
            first.start <= second.start <= first.end
            or first.start <= second.end <= first.end
        ):
            overlap_count += 1
    return overlap_count


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

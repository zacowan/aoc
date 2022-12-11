"""Solution code"""
import pathlib
import sys


class Instruction:
    """Wrapper for a noop or addx instruction."""

    def __init__(self, cycles: int = 1, add_amount: int = 0) -> None:
        self.cycles = cycles
        self.add_amount = add_amount


def parse(puzzle_input: str):
    """Parse input."""
    puzzle_input = puzzle_input.strip()
    instructions: list[Instruction] = []
    for line in puzzle_input.splitlines():
        if line == "noop":
            instructions.append(Instruction())
        else:
            add_amount = int(line.split(" ")[1])
            instructions.append(Instruction(2, add_amount))
    return instructions


def handle_update_signal_strength(
    signal_strengths: list[int], cycle_number: int, x_value: int
):
    """Handles checking if a signal strength should be added, and adding it if so."""
    if (cycle_number - 20) % 40 == 0:
        signal_strengths.append(cycle_number * x_value)


def part1(data: list[Instruction]):
    """Solve part 1."""
    cycle_number = 1
    x_value = 1
    signal_strengths: list[int] = []

    for instruction in data:
        for _ in range(instruction.cycles):
            handle_update_signal_strength(signal_strengths, cycle_number, x_value)
            cycle_number += 1
        x_value += instruction.add_amount

    handle_update_signal_strength(signal_strengths, cycle_number, x_value)

    return sum(signal_strengths)


def handle_add_crt_row(crt_rows: list[str], current_row: str, cycle_index: int) -> bool:
    """Handles updating crt_rows. Returns true if a row was added."""
    if (cycle_index + 1) % 40 == 0:
        crt_rows.append(current_row)
        return True

    return False


class CRTRows:
    """Wrapper for crt_rows array for custom printing."""

    def __init__(self, rows: list[str]) -> None:
        self.rows = rows

    def __str__(self) -> str:
        output = ""
        for row in self.rows:
            output += row
            output += "\n"
        return output

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, CRTRows):
            return self.rows == __o.rows

        return False


def part2(data: list[Instruction]):
    """Solve part 2."""
    # x_value also represents the center of the sprite
    x_value = 1
    cycle_index = 0
    crt_rows: list[str] = []
    current_row = ""

    for instruction in data:
        for _ in range(instruction.cycles):
            # Draw pixel in current row
            if cycle_index in [x_value - 1, x_value, x_value + 1]:
                current_row += "#"
            else:
                current_row += "."
            if handle_add_crt_row(crt_rows, current_row, cycle_index):
                current_row = ""
                cycle_index -= 40
            # Progress cycle
            cycle_index += 1
        # Process instruction
        x_value += instruction.add_amount

    return CRTRows(crt_rows)


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

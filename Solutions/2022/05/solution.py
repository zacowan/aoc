"""Solution code"""
import pathlib
import sys
from collections import deque
import math


class Instruction:
    """Wrapper for instructions."""

    def __init__(self, pick_up_index: int, drop_off_index: int, amount: int) -> None:
        self.pick_up_index = pick_up_index
        self.drop_off_index = drop_off_index
        self.amount = amount

    def __str__(self) -> str:
        return f"move {self.amount} from {self.pick_up_index + 1} to {self.drop_off_index + 1}"


def parse(puzzle_input: str):
    """Parse input."""
    completed_stacks = False
    stacks: list[deque[str]] = []
    instructions: list[Instruction] = []
    for line in puzzle_input.splitlines():
        # Parse stacks
        if completed_stacks is False:
            segment_start, segment_end = 0, 3
            # Check if done with stacks
            if line[segment_start:segment_end].strip() == "1":
                completed_stacks = True
                continue
            # Make sure there are enough stacks
            while math.ceil(len(line) / 4.0) > len(stacks):
                stacks.append(deque())
            while segment_end <= len(line):
                segment = line[segment_start:segment_end]
                if segment.strip():
                    stacks[segment_start // 4].appendleft(segment[1])
                segment_start += 4
                segment_end += 4
        # Parse instructions
        elif line:
            words = line.split(" ")
            amount, pick_up_index, drop_off_index = (
                int(words[1]),
                int(words[3]) - 1,
                int(words[5]) - 1,
            )
            instructions.append(Instruction(pick_up_index, drop_off_index, amount))
    return (stacks, instructions)


def part1(data: tuple[list[deque[str]], list[Instruction]]):
    """Solve part 1."""
    stacks, instructions = data[0], data[1]
    for instruction in instructions:
        for _ in range(instruction.amount):
            popped = stacks[instruction.pick_up_index].pop()
            stacks[instruction.drop_off_index].append(popped)
    result = ""
    for stack in stacks:
        result += stack.pop()
    return result


def part2(data: tuple[list[deque[str]], list[Instruction]]):
    """Solve part 2."""
    stacks, instructions = data[0], data[1]
    for instruction in instructions:
        print(stacks)
        print(instruction)
        to_append: deque[str] = deque()
        for i in range(instruction.amount):
            print(i)
            popped = stacks[instruction.pick_up_index].pop()
            to_append.appendleft(popped)
        for _ in range(instruction.amount):
            popped = to_append.popleft()
            stacks[instruction.drop_off_index].append(popped)
    result = ""
    for stack in stacks:
        result += stack.pop()
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

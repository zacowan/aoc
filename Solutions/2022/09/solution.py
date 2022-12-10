"""Solution code"""
import pathlib
import sys
from enum import Enum


class Direction(Enum):
    """Wrapper for direction."""

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Move:
    """Wrapper for a move."""

    def __init__(self, direction: str, amount: str) -> None:
        if direction == "U":
            self.direction = Direction.UP
        elif direction == "R":
            self.direction = Direction.RIGHT
        elif direction == "D":
            self.direction = Direction.DOWN
        else:
            self.direction = Direction.LEFT
        self.amount = int(amount)


class Knot:
    """Wrapper for head/tail."""

    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def move_one(self, direction: Direction):
        if direction == Direction.UP:
            self.y += -1
        elif direction == Direction.RIGHT:
            self.x += 1
        elif direction == Direction.DOWN:
            self.y += 1
        else:
            self.x += -1

    def get_position(self) -> tuple[int, int]:
        return (self.x, self.y)

    def move_to(self, position: tuple[int, int]):
        self.x = position[0]
        self.y = position[1]


def check_touching(first: Knot, second: Knot) -> bool:
    """Checks if the two knots are touching."""
    if abs(first.x - second.x) <= 1 and abs(first.y - second.y) <= 1:
        return True

    return False


def parse(puzzle_input: str):
    """Parse input."""
    puzzle_input = puzzle_input.strip()
    moves: list[Move] = []
    for line in puzzle_input.splitlines():
        split_line = line.split(" ")
        move = Move(split_line[0], split_line[1])
        moves.append(move)
    return moves


def part1(data: list[Move]):
    """Solve part 1."""
    head, tail = Knot(), Knot()
    visited: set[tuple[int, int]] = set([head.get_position()])
    prev_head_position = head.get_position()

    for move in data:
        for _ in range(move.amount):
            prev_head_position = head.get_position()
            head.move_one(move.direction)
            if not check_touching(head, tail):
                tail.move_to(prev_head_position)
                visited.add(prev_head_position)

    return len(visited)


def determine_new_knot_location(move_knot: Knot, touch_knot: Knot) -> tuple[int, int]:
    """Returns the new location the knot should move to be touching."""
    x_distance = abs(touch_knot.x - move_knot.x)
    y_distance = abs(touch_knot.y - move_knot.y)
    if (x_distance > 1 and y_distance >= 1) or (x_distance >= 1 and y_distance > 1):
        # Move diagonally
        x_direction = (touch_knot.x - move_knot.x) / abs(touch_knot.x - move_knot.x)
        y_direction = (touch_knot.y - move_knot.y) / abs(touch_knot.y - move_knot.y)
        return (move_knot.x + x_direction, move_knot.y + y_direction)
    elif x_distance > 1:
        # Move horizontally
        direction = (touch_knot.x - move_knot.x) / abs(touch_knot.x - move_knot.x)
        return (move_knot.x + direction, move_knot.y)
    else:
        # Move vertically
        direction = (touch_knot.y - move_knot.y) / abs(touch_knot.y - move_knot.y)
        return (move_knot.x, move_knot.y + direction)


def move_knots(knots: list[Knot], visited: set[tuple[int, int]]):
    """Handles moving the knots that are not touching, if necessary."""
    for i in range(1, len(knots)):
        if not check_touching(knots[i - 1], knots[i]):
            position = determine_new_knot_location(knots[i], knots[i - 1])
            knots[i].move_to(position)
            if i == 8:
                visited.add(knots[i].get_position())


def part2(data):
    """Solve part 2.

    Key concept needed to solve: a piece can be at most 2 units away in BOTH the x and y directions.
    """
    num_knots = 9
    head = Knot()
    knots: list[Knot] = []
    visited: set[tuple[int, int]] = set([head.get_position()])
    prev_head_position = head.get_position()

    for _ in range(num_knots):
        knot = Knot()
        knots.append(knot)

    for move in data:
        for _ in range(move.amount):
            prev_head_position = head.get_position()
            head.move_one(move.direction)
            if not check_touching(head, knots[0]):
                knots[0].move_to(prev_head_position)
                move_knots(knots, visited)

    return len(visited)


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

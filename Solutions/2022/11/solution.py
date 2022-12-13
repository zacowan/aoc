"""Solution code"""
import pathlib
import sys


class PassTest:
    """Wrapper for pass test."""

    def __init__(self) -> None:
        self.divisible_by: int = -1
        self.to_true: int = -1
        self.to_false: int = -1

    def __str__(self) -> str:
        tab = "  "
        string = f"Test: divisible by {self.divisible_by}\n"
        string += f"{tab}If true: throw to monkey {self.to_true}\n"
        string += f"{tab}If false: throw to monkey {self.to_false}\n"
        return string


class Monkey:
    """Wrapper for monkey data."""

    def __init__(self) -> None:
        self.items: list[int] = []
        self.operation: str = None
        self.test: PassTest = None

    def set_items(self, items: list[str]):
        """Sets the items based on list of strings from input."""
        for item in items:
            if item.strip():
                self.items.append(int(item.strip()))

    def add_item(self, item: int):
        """Adds an item to the monkey."""
        self.items.append(item)

    def get_test_result(self, worry: int) -> int:
        """Runs the test and returns which monkey to throw to."""
        result = worry % self.test.divisible_by == 0
        if result:
            return self.test.to_true
        else:
            return self.test.to_false

    def get_worry_after_operation(self, item: int, divide_by_three: bool = True) -> int:
        """Performs the operation and returns the worry."""
        # new = old OP Y
        operation_parts = self.operation.split(" ")
        op = operation_parts[1]
        y = -1
        if operation_parts[0] == operation_parts[2]:
            y = item
        else:
            y = int(operation_parts[2])

        result = 0

        if op == "+":
            result = item + y
        else:
            result = item * y

        if divide_by_three:
            return result // 3
        else:
            return result

    def __str__(self) -> str:
        lines: list[str] = []
        # Add items
        line = "Starting items: "
        for item in self.items:
            line += str(item) + ", "
        line = line[:-2]
        lines.append(line)
        # Add operation
        line = "Operation: new = "
        line += self.operation
        lines.append(line)
        # Add test
        line = str(self.test)
        lines.append(line)
        # Build string
        string = ""
        for line in lines:
            string += line + "\n"
        return string


def parse(puzzle_input: str):
    """Parse input."""
    puzzle_input = puzzle_input.strip()
    lines_per_monkey = 7
    monkeys: list[Monkey] = []
    current_monkey: Monkey
    current_test: PassTest
    for i, line in enumerate(puzzle_input.splitlines()):
        line = line.strip()
        if i % lines_per_monkey == 0:
            current_monkey = Monkey()
            current_test = PassTest()
        elif i % lines_per_monkey == 1:
            line = line[16:]
            items = line.strip().split(", ")
            current_monkey.set_items(items)
        elif i % lines_per_monkey == 2:
            line = line[17:]
            current_monkey.operation = line.strip()
        elif i % lines_per_monkey == 3:
            line = line[19:]
            current_test.divisible_by = int(line.strip())
        elif i % lines_per_monkey == 4:
            line = line[25:]
            current_test.to_true = int(line.strip())
        elif i % lines_per_monkey == 5:
            line = line[25:]
            current_test.to_false = int(line.strip())
        else:
            current_monkey.test = current_test
            monkeys.append(current_monkey)
    # Add last monkey
    current_monkey.test = current_test
    monkeys.append(current_monkey)
    for monkey in monkeys:
        print(monkey)
    return monkeys


def perform_round_part1(monkeys: list[Monkey], inspected_count: dict):
    """Performs a single round."""
    for i, monkey in enumerate(monkeys):
        for item in monkey.items:
            inspected_count[i] += 1
            worry = monkey.get_worry_after_operation(item)
            to_throw_to = monkey.get_test_result(worry)
            monkeys[to_throw_to].add_item(worry)
        monkey.items = []


def part1(data: list[Monkey]):
    """Solve part 1."""
    rounds = 20
    inspected_count: dict = {}
    for i in range(len(data)):
        inspected_count[i] = 0
    for _ in range(rounds):
        perform_round_part1(data, inspected_count)
    values = inspected_count.values()
    values = sorted(values, reverse=True)
    return values[0] * values[1]


def perform_round_part2(monkeys: list[Monkey], inspected_count: dict):
    """Performs a single round."""
    for i, monkey in enumerate(monkeys):
        print(f"Monkey {i}")
        print(monkey)
        for item in monkey.items:
            inspected_count[i] += 1
            worry = monkey.get_worry_after_operation(item, False)
            to_throw_to = monkey.get_test_result(worry)
            monkeys[to_throw_to].add_item(worry)
        monkey.items = []


def part2(data: list[Monkey]):
    """Solve part 2.
    Chinese remainder theorem??
    """
    rounds = 10000
    inspected_count: dict = {}
    for i in range(len(data)):
        inspected_count[i] = 0
    for _ in range(rounds):
        perform_round_part2(data, inspected_count)
    values = inspected_count.values()
    values = sorted(values, reverse=True)
    return (values[0] * rounds * len(data)) * (values[1] * rounds * len(data))


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

"""Solution code"""
import pathlib
import sys
from enum import IntEnum


class Choice(IntEnum):
    """Enum of choices for RPS."""

    UNKNOWN = 0
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(IntEnum):
    """Enum of round outcomes."""

    UNKNOWN = -1
    LOSE = 0
    DRAW = 1
    WIN = 2


CHOICE_MAPPING = {
    "A": Choice.ROCK,
    "X": Choice.ROCK,
    "B": Choice.PAPER,
    "Y": Choice.PAPER,
    "C": Choice.SCISSORS,
    "Z": Choice.SCISSORS,
}

OUTCOME_MAPPING = {"X": Outcome.LOSE, "Y": Outcome.DRAW, "Z": Outcome.WIN}


class RoundResult:
    """Result of a particular round."""

    def __init__(self, opponent: str, you: str) -> None:
        self.opponent_choice = CHOICE_MAPPING.get(opponent, Choice.UNKNOWN)
        self.you_choice = CHOICE_MAPPING.get(you, Choice.UNKNOWN)
        self.target_outcome = OUTCOME_MAPPING.get(you, Outcome.UNKNOWN)

    def get_choice(self):
        """Returns the choice based on the target outcome."""
        if self.target_outcome == Outcome.LOSE:
            if self.opponent_choice == Choice.ROCK:
                return Choice.SCISSORS
            elif self.opponent_choice == Choice.PAPER:
                return Choice.ROCK
            elif self.opponent_choice == Choice.SCISSORS:
                return Choice.PAPER
            else:
                return Choice.UNKNOWN
        elif self.target_outcome == Outcome.DRAW:
            return self.opponent_choice
        elif self.target_outcome == Outcome.WIN:
            if self.opponent_choice == Choice.ROCK:
                return Choice.PAPER
            elif self.opponent_choice == Choice.PAPER:
                return Choice.SCISSORS
            elif self.opponent_choice == Choice.SCISSORS:
                return Choice.ROCK
            else:
                return Choice.UNKNOWN
        else:
            return Choice.UNKNOWN

    def get_outcome(self):
        """Returns the outcome based on choices."""
        outcome = Outcome.LOSE
        if self.you_choice == Choice.ROCK:
            if self.opponent_choice == Choice.SCISSORS:
                outcome = Outcome.WIN
            elif self.opponent_choice == Choice.ROCK:
                outcome = Outcome.DRAW
        elif self.you_choice == Choice.PAPER:
            if self.opponent_choice == Choice.ROCK:
                outcome = Outcome.WIN
            elif self.opponent_choice == Choice.PAPER:
                outcome = Outcome.DRAW
        elif self.you_choice == Choice.SCISSORS:
            if self.opponent_choice == Choice.PAPER:
                outcome = Outcome.WIN
            elif self.opponent_choice == Choice.SCISSORS:
                outcome = Outcome.DRAW
        return outcome


def parse(puzzle_input: str):
    """Parse input."""
    round_results = []
    for line in puzzle_input.splitlines():
        choices = line.split(" ")
        if len(choices) == 2:
            opponent = choices[0]
            you = choices[1]
            round_result = RoundResult(opponent, you)
            round_results.append(round_result)
    return round_results


def part1(data: list[RoundResult]):
    """Solve part 1."""
    total_score = 0
    for result in data:
        score = result.you_choice.value + (result.get_outcome().value * 3)
        total_score += score
    return total_score


def part2(data: list[RoundResult]):
    """Solve part 2."""
    total_score = 0
    for result in data:
        score = result.get_choice() + (result.target_outcome.value * 3)
        total_score += score
    return total_score


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

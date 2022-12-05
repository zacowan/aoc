import pathlib
import pytest
import solution

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return solution.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return solution.parse(puzzle_input)


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert solution.part1(example1) == 2


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert solution.part2(example1) == 4


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert solution.part2(example2) == ...

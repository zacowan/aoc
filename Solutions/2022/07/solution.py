"""Solution code"""
import pathlib
import sys
from collections import deque


class File:
    """File node."""

    def __init__(self, name: str, extension: str, size: int) -> None:
        self.name = name
        self.extension = extension
        self.size = size

    def __str__(self) -> str:
        dot = "." if self.extension else ""
        return f"{self.name}{dot}{self.extension} (file, size={self.size})"


class Directory:
    """Directory node."""

    def __init__(self, name: str, parent=None) -> None:
        self.name = name
        self.parent = parent
        self.files: list[File] = []
        self.children: list[Directory] = []

    def get_size(self):
        size = 0
        for file in self.files:
            size += file.size
        for directory in self.children:
            size += directory.get_size()
        return size

    def __str__(self) -> str:
        return f"{self.name} (dir)"


def parse_ls_output(line: str, current_directory: Directory):
    """Parses a single line of output from a ls command."""
    split_line = line.split(" ")
    if split_line[0] == "dir":
        # Add sub directory
        directory = Directory(split_line[1], current_directory)
        current_directory.children.append(directory)
    else:
        # Add file
        name_extension = split_line[1].split(".")
        name = name_extension[0]
        extension = ""
        if len(name_extension) > 1:
            extension = name_extension[1]
        file = File(name, extension, int(split_line[0]))
        current_directory.files.append(file)


def parse_cd_command(
    line: str, current_directory: Directory, root_directory: Directory
):
    """Parses a cd command and returns the new current directory."""
    target = line.split(" ")[2]
    if target == "/":
        return root_directory
    elif target == "..":
        return current_directory.parent
    else:
        for directory in current_directory.children:
            if directory.name == target:
                return directory


def print_directory_recursive(root_directory: Directory, tabs: int = 0):
    """Prints the entire tree from the root."""
    tab = "  "
    tabs_string = tab * tabs
    print(f"{tabs_string}- {str(root_directory)}\n")
    tabs += 1
    tabs_string = tab * tabs
    for file in root_directory.files:
        print(f"{tabs_string}- {str(file)}\n")
    for directory in root_directory.children:
        print_directory_recursive(directory, tabs)


def parse(puzzle_input: str):
    """Parse input."""
    root_directory = Directory("/")
    current_directory = root_directory
    for line in puzzle_input.strip().splitlines():
        if line == "$ cd /" or line == "$ ls":
            continue
        elif line[0] == "$":
            current_directory = parse_cd_command(
                line, current_directory, root_directory
            )
        else:
            parse_ls_output(line, current_directory)
    return root_directory


def part1(root: Directory) -> int:
    """Solve part 1."""
    MAX_SIZE = 100000
    total_sizes_within_max = 0
    root_size = root.get_size()
    if root_size <= MAX_SIZE:
        total_sizes_within_max += root_size
    for directory in root.children:
        total_sizes_within_max += part1(directory)
    return total_sizes_within_max


def part2(root: Directory) -> int:
    """Solve part 2."""
    FILESYSTEM_SIZE = 70000000
    UPDATE_SIZE = 30000000
    total_size = root.get_size()
    directory_sizes: list[int] = []
    queue = deque([root])
    while len(queue) > 0:
        directory = queue.popleft()
        directory_sizes.append(directory.get_size())
        for child in directory.children:
            queue.append(child)
    available_space = FILESYSTEM_SIZE - total_size
    target_delete_space = UPDATE_SIZE - available_space
    directory_sizes.sort()
    for size in directory_sizes:
        if size >= target_delete_space:
            return size
    return -1


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

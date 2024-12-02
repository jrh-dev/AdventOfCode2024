"""
Day 01 of Advent of Code 2024
"""

from typing import List


def _standard_parse(puzzle_input: str) -> List[List[int, int]]:
    puzzle_input = puzzle_input.split("\n")
    puzzle_input = [i.split("  ") for i in puzzle_input]
    return puzzle_input


def solve_p1(puzzle_input: List[List[int, int]]) -> int:
    """
    Solve the first part of the puzzle.
    """
    sorted_left = sorted([int(i[0]) for i in puzzle_input])
    sorted_right = sorted([int(i[1]) for i in puzzle_input])

    distance = 0
    for i in zip(sorted_left, sorted_right):
        distance += abs(i[1] - i[0])

    return distance


def solve_p2(puzzle_input: List[List[int, int]]) -> int:
    """
    Solve the second part of the puzzle.
    """
    left = [int(i[0]) for i in puzzle_input]
    right = [int(i[1]) for i in puzzle_input]
    distance = 0
    for i in left:
        distance += i * right.count(i)
    return distance


if __name__ == "__main__":
    with open("./d01_dummy.txt", encoding="utf-8") as d, open(
        "./d01_full.txt", encoding="utf-8"
    ) as f:
        d_input = _standard_parse(d.read())
        f_input = _standard_parse(f.read())
    print(f"Part 1 dummy input solution {solve_p1(d_input)}")
    print(f"Part 1 full input solution {solve_p1(f_input)}")
    print(f"Part 2 dummy input solution {solve_p2(d_input)}")
    print(f"Part 2 full input solution {solve_p2(f_input)}")

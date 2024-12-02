"""
Day 02 of Advent of Code 2024
"""
from typing import List

def _standard_parse(puzzle_input: str) -> List[List[int]]:
    return [[int(j) for j in i.split(" ")] for i in puzzle_input.split("\n")]


def valid_asc(seq: List[int], tolerence: int, allow_skip: bool) -> bool:
    for i in range(1, len(seq)):
        if not (seq[i] > seq[i - 1] and seq[i] < (seq[i - 1] + tolerence + 1)):
            if allow_skip:
                for i in range(0, len(seq)):
                    adj_seq = seq[:]
                    del adj_seq[i]
                    if valid_asc(adj_seq, tolerence, False):
                        return True
            return False
    return True

def valid_desc(seq: List[int], tolerence: int, allow_skip: bool) -> bool:
    for i in range(1, len(seq)):
        if not(seq[i] < seq[i - 1] and seq[i] > (seq[i - 1] - tolerence - 1)):
            if allow_skip:
                for i in range(0, len(seq)):
                    adj_seq = seq[:]
                    del adj_seq[i]
                    if valid_desc(adj_seq, tolerence, False):
                        return True
            return False
    return True


def solver(puzzle_input: List[List[int]], tolerence: int, allow_skip: bool) -> int:
    """
    Solve the first part of the puzzle.
    """
    valid = 0
    for i in puzzle_input:
        if valid_asc(i, tolerence, allow_skip) or valid_desc(i, tolerence, allow_skip):
            valid += 1
    return valid


if __name__ == "__main__":
    with open("./d02_dummy.txt", encoding="utf-8") as d, open(
        "./d02_full.txt", encoding="utf-8"
    ) as f:
        d_input = _standard_parse(d.read())
        f_input = _standard_parse(f.read())
    print(f"Part 1 dummy input solution {solver(d_input, 3, False)}")
    print(f"Part 1 full input solution {solver(f_input, 3, False)}")
    print(f"Part 2 dummy input solution {solver(d_input, 3, True)}")
    print(f"Part 2 full input solution {solver(f_input, 3, True)}")

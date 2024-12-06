import re
from typing import Tuple

with open("./d06_full.txt", encoding="utf-8") as f:
    ip = f.read().split("\n")

y_bound = (0, len(ip) - 1)
x_bound = (0, len(ip[0]) - 1)
divmod_len = x_bound[1] + 1
ns_move = len(ip)
coip = "".join(ip)
cur_loc = [loc.span()[0] for loc in re.finditer(r"\^", coip)][0]


def feasible(c: Tuple[int,int], n: Tuple[int,int]) -> bool:
    "check if the move is feasible"
    if (abs(c[0] - n[0]) > 1) | (abs(c[1] - n[1]) > 1) | (n[0] < y_bound[0]) | (n[0] > y_bound[1]) | (n[1] < x_bound[0]) | (n[1] > x_bound[1]):
        return False
    return True


def runner(ip: str, cur_loc: int) -> Tuple[int, set, bool]:
    """
    Map traversal and recording for parts 1 and 2
    """
    moves = [cur_loc]
    direction = "n"
    turns = []

    dirs = {
        "n": (-ns_move, "e"),
        "e": (1, "s"),
        "s": (ns_move, "w"),
        "w": (-1, "n"),
    }

    while True:
        if len(set(turns)) < len(turns):
            return(len(set(moves)), set(moves), True)
        m, n = dirs[direction]
        try_loc = cur_loc + m
        if not feasible(divmod(cur_loc, divmod_len), divmod(try_loc, divmod_len)):
            return(len(set(moves)), set(moves), False)
        if ip[try_loc] == "#":
            direction = n
            turns.append(hash((cur_loc, direction)))
        else:
            cur_loc = try_loc
            moves.append(cur_loc)

p1, full_path, _ = runner(coip, cur_loc)

loops = []
for m in [fp for fp in full_path if fp != cur_loc]:
    _, _, loop = runner(coip[:m] + "#" + coip[m + 1:], cur_loc)
    loops.append(loop)

p2 = sum(loops)

print(f"Part 1 solution: {p1}")
print(f"Part 2 solution: {p2}")

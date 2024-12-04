import re


def feasible_gen(y_bounds: tuple, x_bounds: tuple):
    """Generate a function to check if a coordinate is within the bounds of the matrix."""

    def feasible(y: int, x: int) -> bool:
        return y_bounds[0] <= y <= y_bounds[1] and x_bounds[0] <= x <= x_bounds[1]

    return feasible


def part_one(puzzle_input: str) -> int:
    """solve the first part of the puzzle"""

    matrix = puzzle_input.strip().split("\n")
    divmod_len = len(matrix)
    feasible = feasible_gen(
        (0, len(puzzle_input.strip().split("\n")) - 1),
        (0, len(puzzle_input.strip().split("\n")[0]) - 1),
    )

    result = 0

    for l in [
        loc.span()[0] for loc in re.finditer("X", puzzle_input.replace("\n", ""))
    ]:
        y, x = divmod(l, divmod_len)
        locs = [
            ((y - 1, x, "M"), (y - 2, x, "A"), (y - 3, x, "S")),
            ((y - 1, x + 1, "M"), (y - 2, x + 2, "A"), (y - 3, x + 3, "S")),
            ((y, x + 1, "M"), (y, x + 2, "A"), (y, x + 3, "S")),
            ((y + 1, x + 1, "M"), (y + 2, x + 2, "A"), (y + 3, x + 3, "S")),
            ((y + 1, x, "M"), (y + 2, x, "A"), (y + 3, x, "S")),
            ((y + 1, x - 1, "M"), (y + 2, x - 2, "A"), (y + 3, x - 3, "S")),
            ((y, x - 1, "M"), (y, x - 2, "A"), (y, x - 3, "S")),
            ((y - 1, x - 1, "M"), (y - 2, x - 2, "A"), (y - 3, x - 3, "S")),
        ]
        for m, a, s in locs:
            if feasible(m[0], m[1]) and feasible(a[0], a[1]) and feasible(s[0], s[1]):
                if (
                    matrix[m[0]][m[1]] == m[2]
                    and matrix[a[0]][a[1]] == a[2]
                    and matrix[s[0]][s[1]] == s[2]
                ):
                    result += 1

    return result


def part_two(puzzle_input: str) -> int:
    """solve the second part of the puzzle"""

    matrix = puzzle_input.strip().split("\n")
    divmod_len = len(matrix)
    feasible = feasible_gen(
        (0, len(puzzle_input.strip().split("\n")) - 1),
        (0, len(puzzle_input.strip().split("\n")[0]) - 1),
    )

    result = 0

    for l in [
        loc.span()[0] for loc in re.finditer("A", puzzle_input.replace("\n", ""))
    ]:
        y, x = divmod(l, divmod_len)

        locs = [
            (
                (y - 1, x - 1, "M"),
                (y + 1, x + 1, "S"),
                (y + 1, x - 1, "S"),
                (y - 1, x + 1, "M"),
            ),
            (
                (y - 1, x - 1, "M"),
                (y + 1, x + 1, "S"),
                (y + 1, x - 1, "M"),
                (y - 1, x + 1, "S"),
            ),
            (
                (y - 1, x - 1, "S"),
                (y + 1, x + 1, "M"),
                (y + 1, x - 1, "S"),
                (y - 1, x + 1, "M"),
            ),
            (
                (y - 1, x - 1, "S"),
                (y + 1, x + 1, "M"),
                (y + 1, x - 1, "M"),
                (y - 1, x + 1, "S"),
            ),
        ]
        for m1, s1, m2, s2 in locs:
            if (
                feasible(m1[0], m1[1])
                and feasible(s1[0], s1[1])
                and feasible(m2[0], m2[1])
                and feasible(s2[0], s2[1])
            ):
                if (
                    matrix[m1[0]][m1[1]] == m1[2]
                    and matrix[s1[0]][s1[1]] == s1[2]
                    and matrix[m2[0]][m2[1]] == m2[2]
                    and matrix[s2[0]][s2[1]] == s2[2]
                ):
                    result += 1
    return result


if __name__ == "__main__":
    with open("./d04_dummy.txt", encoding="utf-8") as d, open(
        "./d04_full.txt", encoding="utf-8"
    ) as f:
        d_input = d.read()
        f_input = f.read()

    print(f"Part 1 dummy input solution {part_one(d_input)}")
    print(f"Part 1 full input solution {part_one(f_input)}")
    print(f"Part 2 dummy input solution {part_two(d_input)}")
    print(f"Part 2 full input solution {part_two(f_input)}")

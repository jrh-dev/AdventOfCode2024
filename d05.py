def parser(puzzle_input: str) -> tuple:
    """
    Parse the puzzle input
    """
    i, l = puzzle_input.split("\n\n")
    return _parse_instructions(l), _parse_lookup(i)

def _parse_instructions(puzzle_input: str) -> list:
    puzzle_input = puzzle_input.split("\n")
    puzzle_input = [i.split(",") for i in puzzle_input]
    puzzle_input = [[int(j) for j in i] for i in puzzle_input]
    return puzzle_input

def _parse_lookup(puzzle_input: str) -> dict:
    rules = puzzle_input.split("\n")
    pages = list(set(r.split("|")[0] for r in rules))
    lookup = {}
    for p in pages:
        lookup[p] = [int(r.split("|")[1]) for r in rules if r.split("|")[0] == p]
    return lookup


def solver(instructs: list, lookup: dict) -> tuple:
    """
    Solve both parts of the problem for day 5
    """
    part_one_total = 0
    part_two_total = 0
    for this in instructs:
        that = []
        for i in this:
            constraints = lookup[str(i)] if str(i) in lookup else []
            insert_at = min([that.index(j) for j in constraints if j in that] + [len(that)])
            that.insert(insert_at, i)
        if that == this:
            part_one_total += this[divmod(len(this), 2)[0]]
        else:
            part_two_total += that[divmod(len(that), 2)[0]]
    return part_one_total, part_two_total

if __name__ == "__main__":
    with open("./d05_full.txt", encoding="utf-8") as f:
        d_input = f.read()
    parsed_instructs, order_lookup = parser(d_input)
    p1, p2 = solver(parsed_instructs, order_lookup)

    print(f"Part solution: {p1}")
    print(f"Part solution: {p2}")

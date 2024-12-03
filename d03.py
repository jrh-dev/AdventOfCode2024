import re


TEST_INPUT_P1 = (
    "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
)
TEST_INPUT_P2 = (
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
)


def solver(input, complex: bool):
    """
    Solve both parts of the problem for day 3
    """
    PATTERN = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"
    total = 0
    enabled = True

    for match in re.findall(PATTERN, input):
        if "mul" in match and enabled:
            res = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", match)[0]
            total += int(res[0]) * int(res[1])
        elif "do()" in match and complex:
            enabled = True
        elif "don't()" in match and complex:
            enabled = False

    return total


if __name__ == "__main__":
    with open("./d03_full.txt", encoding="utf-8") as f:
        f_input = f.read()

    solver(TEST_INPUT_P1, False)
    solver(f_input, False)
    solver(TEST_INPUT_P2, True)
    solver(f_input, True)

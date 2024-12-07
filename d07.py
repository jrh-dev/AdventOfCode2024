from typing import List

def solver(elements: List[int], ans: int, enable_combine: bool) -> int:
    """
    This function is used to solve the problem for day 7.    
    """
    queue = [elements.pop(0)]
    cq = []
    for e in elements:
        mq = [q * e for q in queue]
        aq = [q + e for q in queue]
        if enable_combine:
            cq = [int(str(q) + str(e)) for q in queue]
        queue = list(set(q for q in mq + aq + cq if q <= ans))
        if len(queue) == 0:
            break
    return ans if ans in queue else 0


if __name__ == "__main__":
    with open("./d07_full.txt", encoding="utf-8") as f:
        ip = [ip.split(": ") for ip in f.read().split("\n")]

    p1_ans, p2_ans = [], []

    for i in ip:
        elements_arg = [int(n) for n in i[1].split(" ")]
        ans_arg = int(i[0])
        p1_ans.append(solver(elements_arg[:], ans_arg, False))
        p2_ans.append(solver(elements_arg[:], ans_arg, True))

    print(f"Part 1 solution: {sum(p1_ans)}")
    print(f"Part 2 solution: {sum(p2_ans)}")

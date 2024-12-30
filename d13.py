import re

def push_it(Ax, Ay, Bx, By, Px, Py):
    i = By * Px - Bx * Py
    j = -Ay * Px + Ax * Py
    k = (Ax * By) - (Ay * Bx)
    if k == 0 or i % k != 0 or j % k != 0:
        return None
    else:
        return 3 * i / k + j / k

if __name__ == "__main__":
    with open("./d13_full.txt", encoding="utf-8") as f:
        ip = f.read().split("\n\n")
    offset = 10000000000000
    ans_p1 = []
    ans_p2 = []
    for i in ip:
        i = i.split("\n")
        Ax, Ay = map(int, "".join(re.findall(r"[0-9,]", i[0])).split(","))
        Bx, By = map(int, "".join(re.findall(r"[0-9,]", i[1])).split(","))
        Px, Py = map(int, "".join(re.findall(r"[0-9,]", i[2])).split(","))
        ans_p1.append(push_it(Ax, Ay, Bx, By, Px, Py))
        ans_p2.append(push_it(Ax, Ay, Bx, By, Px + offset, Py + offset))   
    print(f"Part 1 solution: {int(sum(i for i in ans_p1 if i is not None))}")
    print(f"Part 2 solution: {int(sum(i for i in ans_p2 if i is not None))}")
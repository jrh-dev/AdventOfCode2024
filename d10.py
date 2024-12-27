import re

with open("./d10_full.txt", encoding="utf-8") as f:
        ip = f.read()

def feasible_gen(y_bounds: tuple, x_bounds: tuple):
    def feasible(y: int, x: int) -> bool:
        return y_bounds[0] <= y <= y_bounds[1] and x_bounds[0] <= x <= x_bounds[1]
    return feasible

matrix = ip.strip().split("\n")
divmod_len = len(matrix)
feasible = feasible_gen(
        (0, len(ip.strip().split("\n")) - 1),
        (0, len(ip.strip().split("\n")[0]) - 1),
    )

trail_heads = [loc.span()[0] for loc in re.finditer("0", ip.replace("\n", ""))]

p1_completed = 0
p2_completed = 0

for th in trail_heads:
    y, x = divmod(th, divmod_len)
    queue = [(y, x)]
    th_completed = []
    while queue:
        y, x = queue.pop(0)
        locs = [
            (y - 1, x),
            (y + 1, x),
            (y, x - 1),
            (y, x + 1),
        ]
        for ty, tx in locs:
            if feasible(ty, tx) and (int(matrix[ty][tx]) - int(matrix[y][x]) == 1):
                if matrix[ty][tx] == "9":
                    th_completed.append((ty,tx))
                else:
                    queue.append((ty,tx))
    p1_completed += len(set(th_completed))
    p2_completed += len(th_completed)

print(f"Part 1 full input solution {p1_completed}")
print(f"Part 2 full input solution {p2_completed}")



with open("./d12_full.txt", encoding="utf-8") as f:
        ip = f.read()

def feasible_gen(y_bounds: tuple, x_bounds: tuple):
    def feasible(y: int, x: int) -> bool:
        return y_bounds[0] <= y <= y_bounds[1] and x_bounds[0] <= x <= x_bounds[1]
    return feasible

def check_corners(y,x,coords):
    ne = [(y - 1, x + 1), (y - 1, x), (y, x + 1)]
    se = [(y + 1, x + 1), (y + 1, x), (y, x + 1)]
    sw = [(y + 1, x - 1), (y + 1, x), (y, x - 1)]
    nw = [(y - 1, x - 1), (y - 1, x), (y, x - 1)]
    inside_corners = sum([
        (ne[0] not in coords and ne[1] in coords and ne[2] in coords),
        (se[0] not in coords and se[1] in coords and se[2] in coords),
        (sw[0] not in coords and sw[1] in coords and sw[2] in coords),
        (nw[0] not in coords and nw[1] in coords and nw[2] in coords),
    ])
    outside_corners = sum([
        (ne[1] not in coords and ne[2] not in coords),
        (se[1] not in coords and se[2] not in coords),
        (sw[1] not in coords and sw[2] not in coords),
        (nw[1] not in coords and nw[2] not in coords),
    ])
    return inside_corners + outside_corners

matrix = ip.strip().split("\n")
divmod_len = len(matrix)
feasible = feasible_gen(
        (0, len(ip.strip().split("\n")) - 1),
        (0, len(ip.strip().split("\n")[0]) - 1),
    )

ip_len = len(ip.replace("\n", ""))

total_p1 = 0
total_p2 = 0
visited = []

for ii in range(ip_len):
    y, x = divmod(ii, divmod_len)
    if (y, x) in visited:
        continue
    current_group_p1 = []
    coords = []
    queue = [(y, x)]
    type_is = matrix[y][x]
    while queue:
        y, x = queue.pop(0)
        visited.append((y, x))
        coords.append((y, x))
        locs = [
                (y - 1, x),
                (y + 1, x),
                (y, x - 1),
                (y, x + 1),
            ]
        current_group_p1.append(4 - sum(1 for y, x in locs if feasible(y, x) and matrix[y][x] == type_is))
        for ty, tx in locs:        
            if (ty, tx) not in visited and feasible(ty, tx) and matrix[ty][tx] == type_is and (ty, tx) not in queue:
                queue.append((ty, tx))
    total_p1 += sum(current_group_p1) * len(current_group_p1)
    for c in coords:
        total_p2 += check_corners(c[0], c[1], coords) * len(coords)
    


print(f"Part 1 solution: {total_p1}")
print(f"Part 2 solution: {total_p2}")



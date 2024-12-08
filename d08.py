from itertools import combinations

with open("./d08_full.txt", encoding="utf-8") as f:
    ip = [ip for ip in f.read().split("\n")]

divmod_len = len(ip[0])

ip = "".join(ip)

freqs = set(i for i in ip if i != ".")

freq_d = {c: [divmod(x, divmod_len) for x,y in enumerate(ip) if y == c] for c in freqs}

p1_antinodes = set()
p2_antinodes = set()

for values in freq_d.values():
    for c in combinations(values, r=2):
        y = c[0][0]
        x = c[0][1]
        yc1 = c[0][0] - c[1][0]
        xc1 = c[0][1] - c[1][1]
        yc2 = c[1][0] - c[0][0]
        xc2 = c[1][1] - c[0][1]
        p1_antinodes.add((c[0][0] + yc1, c[0][1] + xc1))
        p1_antinodes.add((c[1][0] + yc2, c[1][1] + xc2))

        while True:
            p2_antinodes.add((y, x))
            y += yc1    
            x += xc1
            if not ((y >= 0) and (x >= 0) and (y < divmod_len) and (x < divmod_len)):
                break

        y = c[0][0]
        x = c[0][1]

        while True:
            p2_antinodes.add((y, x))
            y += yc2
            x += xc2
            if not ((y >= 0) and (x >= 0) and (y < divmod_len) and (x < divmod_len)):
                break
        

p1 = len([a for a in p1_antinodes if (a[0] >= 0) and (a[1] >= 0) and (a[0] < divmod_len) and (a[1] < divmod_len)])
p2 = len(p2_antinodes)

print(f"Part 1 solution: {p1}")
print(f"Part 2 solution: {p2}")

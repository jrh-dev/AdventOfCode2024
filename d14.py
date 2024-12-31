from dataclasses import dataclass
import re
import statistics
from math import prod

@dataclass
class Robot:
    x: int
    y: int
    mx: int
    my: int
    xlim:int  = 101
    ylim: int = 103
    def move(self, n):
        self.x = ((self.x + (self.mx * n)) % self.xlim)
        self.y = ((self.y + (self.my * n)) % self.ylim)

with open("./d14_full.txt", encoding="utf-8") as f:
    ip = f.read().split("\n")

robots = []
for i in ip:
    i = i.split(" ")
    x, y = map(int, "".join(re.findall(r"[0-9,]", i[0])).split(","))
    mx, my = map(int, "".join(re.findall(r"[0-9,-]", i[1])).split(","))
    robots.append(Robot(x, y, mx, my))

for r in robots:
    r.move(100)

midx = 50
midy = 51

ans_p1 = [0] * 4

for r in robots:
    if r.x < midx and r.y < midy:
        ans_p1[0] += 1
    elif r.x < midx and r.y > midy:
        ans_p1[1] += 1
    elif r.x > midx and r.y < midy:
        ans_p1[2] += 1
    elif r.x > midx and r.y > midy:
        ans_p1[3] += 1

ans_p1 = prod(ans_p1)

for s in range(10000):
    for r in robots:        
        r.move(1)
    x_state, y_state = zip(*[(r.x, r.y) for r in robots])
    if statistics.stdev(x_state) < 25 and statistics.stdev(y_state) < 25:
        break

ans_p2 = s + 1

print(f"Part 1 solution: {ans_p1}")
print(f"Part 2 solution: {ans_p2}")


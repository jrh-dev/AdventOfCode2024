
from dataclasses import dataclass

with open("./d09_full.txt", encoding="utf-8") as f:
    pi = f.read()

@dataclass
class File:
    value: int
    size: int

hdd = []

for n,e in enumerate(pi):
    if n % 2 == 0:
        hdd.append(File(value = int((n / 2)), size = int(e)))
    else:
        hdd.append(File(value = int(-1), size = int(e)))

moving = max(f.value for f in hdd)

for ii in range(moving, 0, -1):
    needs = [f.size for f in hdd if f.value == ii][0]
    for n,f in enumerate(hdd):
        if f.value == ii:
            break
        elif f.value == -1 and f.size == needs:
            del hdd[n]
            hdd.insert(n, File(ii, needs))
            for jj in range(n+1, len(hdd)):
                if hdd[jj].value == ii:
                    hdd[jj].value = -1
                    break
            break
        elif f.value == -1 and f.size > needs:
            del hdd[n]
            hdd.insert(n, File(ii, needs))
            hdd.insert(n+1, File(-1, f.size - needs))
            for jj in range(n+1, len(hdd)):
                if hdd[jj].value == ii:
                    hdd[jj].value = -1
                    break
            break

def parse():
    parsed = []
    for f in hdd:
        parsed += [str(f.value)] * f.size
    return parsed

sol = parse()

ans = 0

for n,e in enumerate(sol):
    if e != "-1":
        ans += int(e) * (n)

ans
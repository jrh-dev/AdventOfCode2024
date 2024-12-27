from dataclasses import dataclass

@dataclass
class Stone:
    value: int
    n: int

    def __eq__(self, other):
        return self.value == other
    
def find_index(stones, value):
        for index, stone in enumerate(stones):
            if stone.value == value:
                return index
        return -1

def blink_no_rule(sv):
    return sv * 2024

def blink_split(sv, dl):
    return (str(sv)[:dl//2], str(sv)[dl//2:])

def blink(track):
    blinked = []
    for stone in track:
        if stone.value == 0:
            idx = find_index(blinked, 1)
            if idx == -1:
                blinked.append(Stone(1, stone.n))
            else:
                blinked[idx].n += stone.n
        elif (diglen := len(str(stone.value))) % 2 == 0:
            split_l, split_r = blink_split(stone.value, diglen)
            # left
            idx = find_index(blinked, int(split_l))
            if idx == -1:
                blinked.append(Stone(int(split_l), stone.n))
            else:
                blinked[idx].n += stone.n
            # right
            if split_r != '':
                idx = find_index(blinked, int(split_r))
                if idx == -1:
                    blinked.append(Stone(int(split_r), stone.n))
                else:
                    blinked[idx].n += stone.n
        else:
            new_val = blink_no_rule(stone.value)
            idx = find_index(blinked, new_val)
            if idx == -1:
                blinked.append(Stone(new_val, stone.n))
            else:
                blinked[idx].n += stone.n
    return blinked

def lets_blink(track, blinks):
    for _ in range(blinks):
        track = blink(track)
    return track


if __name__ == "__main__":
    with open("./d11_full.txt", encoding="utf-8") as f:
        ip = f.read()
    track = [Stone(int(i), 1) for i in ip.split(" ")]
    print(f"Part 1 solution: {sum([stone.n for stone in lets_blink(track, 25)])}")
    print(f"Part 2 solution: {sum([stone.n for stone in lets_blink(track, 75)])}")



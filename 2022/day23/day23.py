from collections import deque
import os
import time

def load_input():
    elves = {}
    with open("input", "r") as f:
        for y, line in enumerate(f.read().splitlines()):
            for x, char in enumerate(list(line)):
                if char == "#": elves[(x,y)] = None
    return elves

def draw():
    ys = [y for _, y in elves]
    xs = [x for x, _ in elves]
    ys.append(0)
    xs.append(0)

    for y in range(min(ys), max(ys) +1):
        for x in range(min(xs), max(xs) +1):
            print("#" if (x,y) in elves else ".", end="")
        print()

def will_wait(ex, ey):
    fs = [
        (ex+1, ey+1),
        (ex+1, ey-1),
        (ex-1, ey+1),
        (ex-1, ey-1),
        (ex+1, ey),
        (ex-1, ey),
        (ex, ey+1),
        (ex, ey-1),
    ]
    for fx,fy in fs:
        if (fx,fy) in elves:
            return False
    return True

def is_free(ex, ey, dx, dy):
    if dx == 0:
        ds = [(dx-1, dy),(dx, dy),(dx+1, dy)]
    else:
        ds = [(dx, dy-1),(dx, dy),(dx, dy+1)]
    for dx, dy in ds:
        if (ex+dx,ey+dy) in elves:
            return False 
    return True

directions = deque([(0,-1), (0,1), (-1,0), (1,0)])
elves = load_input()
r = ft = 0
while True:
    r += 1
    moves = {}

    # plan moves
    for ex,ey in elves:
        # all tiles around are free... do nothing
        if will_wait(ex,ey):
            continue
        # cycle through directions for one elf
        for i in range(len(directions)):
            dx,dy = directions[i]
            if is_free(ex, ey, dx, dy):
                nx,ny = ex+dx,ey+dy 
                if (nx,ny) not in moves:
                    moves[(nx,ny)] = []
                moves[(nx,ny)].append((ex,ey))
                break


    # execute moves
    for target, es in moves.items():
        # only move if one elf want to move to this tile
        if len(es) == 1:
            del elves[es[0]]
            elves[target] = None

    # cycle through directions for all elves
    directions.rotate(-1)

    if r == 10:
        ys = [y for _, y in elves]
        xs = [x for x, _ in elves]
        ft = ((max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1)) - len(elves)

    os.system("clear")
    print(f"---round{r}---\n")
    draw()
    time.sleep(0.01)
    if len(moves) == 0:
        break

print("part 1:", ft)
print("part 2:", r)


import os
from collections import defaultdict

def draw(rock, cave):
    os.system("clear")
    for y in range(max(cave.keys(), default=0), -1, -1):
        print("|", end="")
        for x in range(width):
            if rock.collide(x, y):
                print("@", end="")
            elif y in cave and x in cave[y]:
                print("#", end="")
            else:
                print(".", end="")
        print("|", end="")
        print()
    print(f"+{'-' * width}+")

class Rock:
    def __init__(self, x, y, shape):
        self.shape = shape 
        self.x = x
        self.y = y
        self.max_x = max([pos[0] for pos in self.shape])
        self.min_x= min([pos[0] for pos in self.shape])

    def right(self):
        return self.x + self.max_x

    def left(self):
        return self.x + self.min_x

    def bottom(self):
        return self.y

    def collide(self, x, y):
        for pos in self.shape:
            if pos[0] + self.x == x and pos[1] + self.y == y:
                return True
        return False

    def is_free(self, change, cave):
        for pos in self.shape:
            cx, cy = pos[0] + self.x + change[0], pos[1] + self.y + change[1]
            if cx >= width or cx < 0 or cy < 0 or cx in cave[cy]:
                return False
        return True

def detect_cycle(cave, si, ji, height, seen, rocks):
    # snapshot of the 5 last rows
    top_view = [str(x) for y in range(5) for x in sorted(cave[height-y])]
    # create a unique key for each scenario
    key = "".join(top_view) + f"-{si}-{ji}" 
    if key in seen:
        return seen[key]
    else:
        seen[key] = (height, rocks)
    return (-1, -1) 

def simulate(limit):
    ji = 0
    si = 0
    cave = defaultdict(lambda: set())
    max_y = 0
    rock = Rock(2, 3, shapes[si])
    counter = 1
    seen = {}
    added_height = 0
    while counter <= limit:
        jet = jets[ji]

        # move to the right if there is space
        if jet == ">" and rock.is_free((1,0), cave):
            rock.x += 1 
        # move to the left if there is space 
        elif jet == "<" and rock.is_free((-1,0), cave):
            rock.x -= 1 

        # reset jet counter if needed
        ji = ji + 1 if ji < len(jets) -1 else 0

        if not rock.is_free((0,-1), cave):
            # store rock in cave
            for pos in rock.shape:
                rx, ry = pos[0] + rock.x, pos[1]  + rock.y
                cave[ry].add(rx)
                if ry > max_y:
                    max_y = ry 

            # reset shape counter if needed
            si = si + 1 if si < len(shapes) -1 else 0

            old_y, old_counter = detect_cycle(cave, si, ji, max_y, seen, counter)
            if old_y != -1:
                dy = max_y - old_y
                dc = counter - old_counter
                repeat = (limit - counter) // dc
                # just continuing with the current state but save the additional height for later
                added_height += repeat * dy 
                # fast forward the counter
                counter += repeat * dc

            # spawn new rock
            rock = Rock(2, max_y + 4, shapes[counter%5])
            counter += 1

            continue
        else:
            rock.y -= 1

    return max_y + 1 + added_height

shapes= [
        [(0,0), (1,0), (2,0), (3,0)],
        [(1,0), (1,1), (0,1), (2,1), (1,2)],
        [(0,0), (1,0), (2,0), (2,1), (2,2)],
        [(0,0), (0,1), (0,2), (0,3)],
        [(0,0), (1,0), (0,1), (1,1)],
        ]

width = 7

with open("input", "r") as f:
    jets= list(f.read().strip())
    print("part 1:", simulate(2022))
    print("part 2:", simulate(1000000000000))

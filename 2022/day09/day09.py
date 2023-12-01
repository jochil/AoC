import os
import time

def move(direction, pos):
    if direction == "L":
        pos[0] -= 1
    elif direction == "R":
        pos[0] += 1
    if direction == "D":
        pos[1] -= 1
    elif direction == "U":
        pos[1] += 1

overlapping = lambda pos1, pos2: pos1[0] == pos2[0] and pos1[1] == pos2[1]

touching = lambda pos1, pos2: abs(pos1[0] - pos2[0]) <= 1 and abs(pos1[1] - pos2[1]) <= 1

def follow(pos1, pos2):
    # same field or touching  => don't move
    if overlapping(pos1, pos2) or touching(pos1, pos2):
        pass
    # same row or column, but not touching
    elif pos1[0] == pos2[0]:
        pos2[1] += 1 if pos1[1] > pos2[1] else -1
    elif pos1[1] == pos2[1]:
        pos2[0] += 1 if pos1[0] > pos2[0] else -1
    else:
        pos2[0] += 1 if pos1[0] > pos2[0] else -1
        pos2[1] += 1 if pos1[1] > pos2[1] else -1

def draw(knots):
    os.system("clear")
    size = (40, 20)
    for y in range(size[1], -size[1], -1):
        #print(f"{y}\t", end='')
        for x in range(-size[0], size[0]):
            sign = 's' if x == y ==0 else '.' 
            for i, knot in enumerate(knots):
                if knot[0] == x and knot[1] == y:
                    sign = "H" if i == 0 else str(i)
                    break
            print(sign, end='')
        print()

with open("input", "r") as f:
    knots_p1 = [[0,0],[0,0]] 
    knots_p2 = [[0,0] for _ in range(0,10)]
    visit_t = []
    visit_k9 = []

    moves = [line.strip().split() for line in f.readlines()]
    for m in moves:
        direction, steps = m
        for _ in range(0, int(steps)):
            # part 1 - simulation with 1 knot
            # move head
            move(direction, knots_p1[0])
            follow(knots_p1[0], knots_p1[1])
            visit_t.append(f"{knots_p1[0][0]}-{knots_p1[0][1]}")

            # part 2 - simulation with 9 knots
            move(direction, knots_p2[0]) # move head
            for k in range(1, 10):
                pos1 = knots_p2[k-1]
                pos2 = knots_p2[k]
                follow(pos1, pos2)
                if k == 9:
                    visit_k9.append(f"{knots_p2[9][0]}-{knots_p2[9][1]}")
            #draw(knots_p2)
            #time.sleep(0.01)

    print("visited part 1:", len(set(visit_t)))
    print("visited part 2:", len(set(visit_k9)))


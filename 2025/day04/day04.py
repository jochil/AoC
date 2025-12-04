import os

# x,y
matrix = [
    (-1,-1), (-1, 0), (-1, 1),
    (1,-1), (1, 0), (1, 1),
    (0, -1), (0, 1)
]
    
def scan(lines):
    rolls = []
    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            char = line[x]
            if char != "@":
                continue
            count = 0
            for mx,my in matrix:
                cx = mx+x
                cy = my+y
                # skip the border 
                if cx < 0 or cy < 0 or cx >= len(line) or cy >= len(line):
                    continue
                if lines[cy][cx] == "@":
                    count += 1
                if count >= 4:
                    break
            if count < 4:
                rolls.append((x,y))
    return rolls

def part1(lines):
    return len(scan(lines))

def part2(lines):
    # convert line into single chars so it can be modified
    # by lines[y][x]
    lines = [list(line.strip()) for line in lines]
    result = 0
    while True:
        free_rolls = scan(lines)
        if len(free_rolls) == 0:
            break
        result += len(free_rolls)
        # update map
        for x,y in free_rolls:
            lines[y][x] = "."
    return result
                        

wd = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(wd, "input_example1"), "r") as f:
    lines = f.readlines()
    
    print("part1:", part1(lines.copy()))
    print("part2:", part2(lines.copy()))

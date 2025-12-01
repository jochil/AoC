import os
import operator

def part1(lines):
    position = 50
    positions = []
    for line in lines:
        op = operator.sub if line.startswith("L") else operator.add
        value = int(line[1:])
        position = abs(op(position, value) % 100)
        positions.append(position)
    return positions.count(0)


def part2(lines):
    position = 50
    counter = 0
    for line in lines:
        op = operator.sub if line.startswith("L") else operator.add
        value = int(line[1:])
        # go step by step
        for i in range(0, value):
            position = op(position, 1) % 100
            if position == 0:
                counter += 1

    return counter
                        

wd = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(wd, "input_example1"), "r") as f:
    lines = f.readlines()
    
    print("part1:", part1(lines.copy()))
    print("part2:", part2(lines.copy()))

import math

def init(path):
    with open(path) as f:
        lines = [line.strip() for line in f.readlines()]

    inst = lines[0]
    map = {line[0:3]:{"L": line[7:10], "R":line[12:15]} for line in lines[2:]}

    return inst, map

def search(pos, inst, map, end_func):
    step = 0
    while True:
        pos = map[pos][inst[step%len(inst)]]
        if end_func(pos):
            break;
        step +=1

    return step + 1

def part1():
    inst, map = init("input_example1")
    print("part1", search("AAA", inst, map, lambda x: x == "ZZZ"))

def part2():
    inst, map = init("input_example2")
    starts = [k for k in map.keys() if k[2] == "A"]

    lcm = 1
    for pos in starts:
        lcm = math.lcm(lcm, search(pos, inst, map, lambda x: x[2] == "Z"))

    print("part2", lcm)

part1()
part2()

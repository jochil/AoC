import os

def part1(lines):
    listA = []
    listB = []
    for line in lines:
        a, b = line.split()
        listA.append(int(a))
        listB.append(int(b))

    sortedA = sorted(listA)
    sortedB = sorted(listB)
    
    return sum([abs(a - b) for a, b in zip(sortedA, sortedB)])

def part2(lines):
    listA = []
    listB = []
    for line in lines:
        a, b = line.split()
        listA.append(int(a))
        listB.append(int(b))
    
    return sum([a * listB.count(a) for a in listA])
                        

wd = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(wd, "input_example1"), "r") as f:
    lines = f.readlines()
    
    print("part1:", part1(lines.copy()))
    print("part2:", part2(lines.copy()))

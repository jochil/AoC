import os

def part1(lines):
    result = 0
    for line in lines:
        a,b = 0, 0
        batteries = [int (c)for c in line.strip()]
        a = max(batteries[:-1])
        b = max(batteries[batteries.index(a)+1:])
        result += int(f"{a}{b}")
    return result

def part2(lines):
    result = 0
    window = 12
    for line in lines:
        num = "" 
        batteries = [int (c)for c in line.strip()]
        for i in range(window -1, -1, -1):
            a = max(batteries[:len(batteries)-i])
            pos = batteries.index(a)
            # setting new left border
            batteries = batteries[pos+1:]
            num += str(a)
        result += int(num)
    return result
                        

wd = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(wd, "input_example1"), "r") as f:
    lines = f.readlines()
    
    print("part1:", part1(lines.copy()))
    print("part2:", part2(lines.copy()))

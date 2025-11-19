import os
import operator

test = lambda a,b,op : not (1 <= abs(a-b) <= 3) or not op(a,b)

def is_safe(levels):
    # get first direction, doesn't matter if equal, range check will handle
    op = operator.lt if levels[0] < levels[1] else operator.gt
    for i in range(0, len(levels)-1):
        a = levels[i]
        b = levels[i+1]
        if test(a,b,op):
            return False
    return True


def part1(lines):
    safe_reports = 0
    for line in lines:
        levels =[int(l) for l in line.split()]
        if is_safe(levels):
            safe_reports += 1
    return safe_reports


def part2(lines):
    safe_reports = 0
    for line in lines:
        levels =[int(l) for l in line.split()]
        if is_safe(levels):
            safe_reports += 1
        else:
            for i in range(len(levels)):
                newLevels = levels.copy()
                del newLevels[i]
                if is_safe(newLevels):
                    safe_reports += 1
                    break

    return safe_reports
                        

wd = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(wd, "input"), "r") as f:
    lines = f.readlines()
    
    print("part1:", part1(lines.copy()))
    print("part2:", part2(lines.copy()))

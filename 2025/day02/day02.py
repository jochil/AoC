import os

def part1(lines):
    result = 0
    line = lines[0]
    for r in line.split(","):
        start, end = r.split("-")
        for i in range(int(start), int(end) + 1):
            strI = str(i)
            l = len(strI)
            # skip numbers with odd length
            if l & 1 == 1:
                continue
            p1, p2 = strI[:l//2], strI[l//2:]
            if p1 == p2:
                result += i
    return result

def part2(lines):
    result = 0
    line = lines[0]
    for r in line.split(","):
        start, end = r.split("-")
        for i in range(int(start), int(end) + 1):
            strI = str(i)
            l = len(strI)
            for pos in range(1, l//2 + 1):
                # skip, can't be devided into equal parts
                if l % pos != 0:
                    continue
                if strI.count(strI[:pos]) == l//pos:
                    result += i
                    break
    return result
                        

wd = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(wd, "input_example1"), "r") as f:
    lines = f.readlines()
    
    print("part1:", part1(lines.copy()))
    print("part2:", part2(lines.copy()))

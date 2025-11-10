import os

def part1(lines):
    return lines 

def part2(lines):
    return lines
                        

wd = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(wd, "input_example1"), "r") as f:
    lines = f.readlines()
    
    print("part1:", part1(lines.copy()))
    print("part2:", part2(lines.copy()))

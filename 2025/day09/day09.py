import os
from itertools import combinations

def part1(lines):
    tiles = [tuple(map(int, tile.strip().split(","))) for tile in lines]
    pairs = combinations(tiles, 2)
    areas = sorted([(abs(a[0] - b[0]) +1)  * (abs(a[1] - b[1])+1) for a, b in pairs], reverse=True)
    return areas[0]

def part2(lines):
    pass
                        

wd = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(wd, "input_example1"), "r") as f:
    lines = f.readlines()
    
    print("part1:", part1(lines.copy()))
    print("part2:", part2(lines.copy()))

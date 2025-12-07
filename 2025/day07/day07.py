import os
from collections import defaultdict

def part1(lines):
    beams = [lines[0].index("S")]
    splits = 0
    for line in lines:
        for i in range(len(beams)):
            beam = beams[i]
            if line[beam] != "^":
                continue
            # split the beam
            splits += 1
            beams[i] = beam-1 
            beams.append(beam+1)
        beams = list(set(beams))
        
    return splits 

def part2(lines):
    # keep track of the "variants" per beam
    beams = {lines[0].index("S"): 1}
    for line in lines:
        splitted_beams = defaultdict(int)
        for k, v in beams.items():
            if line[k] != "^":
                splitted_beams[k] += v
                continue
            # split the beam
            splitted_beams[k-1] += v
            splitted_beams[k+1] += v
        beams = splitted_beams
        
    return sum(beams[i] for i in beams)
                        

wd = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(wd, "input_example1"), "r") as f:
    lines = f.readlines()
    
    print("part1:", part1(lines.copy()))
    print("part2:", part2(lines.copy()))

block_sums = []
def find(line:str):
    n = [c for c in line if c.isnumeric()]
    return int(n[0] + n[-1])

def part1(lines):
    return sum([find(line) for line in lines])

def part2(lines):
    literals = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    r = 0
    for line in lines:
        for i, l in enumerate(literals):
            line = line.replace(l, f"{l}{i+1}{l}")
        r += find(line)

    print("part2", r)
                        
with open("input", "r") as f:
    lines = f.readlines()

    print("part1:", part1(lines.copy()))
    part2(lines.copy())


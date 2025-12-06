import os
import operator

ops = {
    "+": operator.add,
    "*": operator.mul,
}

def calc(operands, operators):
    total = 0
    for nums, op in zip(operands, operators):
        result = nums[0]
        for n in nums[1:]:
            result = op(result, n)
        total += result
    return total


def part1(lines):
    operators = [ops[o] for o in lines[-1].split()]
    operands = [[] for i in range(len(operators))]

    for line in lines[:-1]:
        for i, o in enumerate(line.strip().split()):
            operands[i].append(int(o))
    
    return calc(operands, operators)
            
        
def part2(lines):
    operators = [ops[o] for o in lines[-1].split()]
    operands = [[] for i in range(len(operators))]

    # how big is each column
    steps = []
    step = 0
    for char in lines[-1]:
        if char != " ":
            if step != 0:
                steps.append(step)
            step = 1
        else:
            step +=1
    steps.append(step) # don't forget the last one
    
    pos = 0
    for i, step in enumerate(steps):
        # go through all columns
        nums = [line[pos:pos+step]for line in lines[:-1]]
        # now each char one by one
        for j in range(max(map(len, nums))):
            r = ""
            for n in nums:
                a = n[j]
                if a != "":
                    r = r + a 
            r = r.strip()
            if r != "":
                operands[i].append(int(r))
        pos += step

    return calc(operands, operators)

wd = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(wd, "input"), "r") as f:
    lines = f.readlines()
    
    print("part1:", part1(lines.copy()))
    print("part2:", part2(lines.copy()))

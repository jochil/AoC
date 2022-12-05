import re
regx_inst = r"move (\d+) from (\d+) to (\d+)"
stacks_p1 = [] 
stacks_p2 = [] 

def parse_start(start):
    # split by line breaks and reverse list 
    # column indices are now first row
    rows = start.split("\n")[::-1]
    # count number of stacks by splitting column indices
    num_stacks = len(rows.pop(0).split("  "))
    for i in range(0, num_stacks):
        stack = []
        for row in rows:
            # position of the letter
            pos = (i * 4) + 1
            crate = row[pos]
            # remove empty ones
            if crate.isupper():
                stack.append(crate)
        stacks_p1.append(stack)
        stacks_p2.append(stack.copy()) # avoid references


with open("input_example", "r") as f:
    # split initial stack layout from instructions
    start, instructions = f.read().split("\n\n")
    parse_start(start)

    for match in re.finditer(regx_inst, instructions, re.MULTILINE):
        number, src, dst = match.groups()
        # work with 0-indexed arrays for each stack
        src = int(src)-1
        dst = int(dst)-1
        number = int(number)

        # part 1: move crate by crate
        for i in range(0, number):
            stacks_p1[dst].append(stacks_p1[src].pop())

        # part 2: move a block of crates
        crates = stacks_p2[src][-number:]
        stacks_p2[dst].extend(crates)
        del stacks_p2[src][-number:]

    print("part 1:", "".join([stack[-1] for stack in stacks_p1]))
    print("part 2:", "".join([stack[-1] for stack in stacks_p2]))
        


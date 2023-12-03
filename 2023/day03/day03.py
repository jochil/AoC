from termcolor import colored

def check(lines, ax, ay):
    grid = [(-1,0), (1, 0), (-1,1), (1,1), (0, 1), (-1,-1), (1,-1), (0, -1)]
    for bx,by in grid:
        x = ax+bx
        y = ay+by
        try:
            c = lines[y][x]
            if c == "*":
                 return 1, x, y
            elif not c.isnumeric() and not c == ".":
                return 0, x,y
        except:
            pass
    return -1, -1, -1

def print_num(num, is_part, is_gear):
    color = "red"
    if is_gear:
        color = "yellow"
    elif is_part:
        color = "green"
    print(colored(num, color), end="")

with open("input") as f:
    lines = [l.strip() for l in f.readlines()]

    parts = []
    gears = {}
    for y in range(len(lines)):
        curr_num = ""
        curr_part = False
        curr_gears = []
        for x in range(len(lines[y])):
            end_num = False
            c = lines[y][x]
            if c.isnumeric():
                curr_num += c
                ch, cx, cy = check(lines, x,y)
                if ch >= 0:
                    curr_part = True
                    if ch == 1:
                        curr_gears.append((cx,cy))
                if x == len(lines[y])-1:
                    end_num = True
            elif curr_num != "": 
                end_num = True

            if end_num:
                print_num(curr_num, curr_part, len(curr_gears)>0)
                if len(curr_gears) > 0 or curr_part:
                    parts.append(int(curr_num))
                for cg in curr_gears:
                    if cg not in gears:
                        gears[cg] = set()
                    gears[cg].add(int(curr_num))
                curr_num = ""
                curr_part = False
                curr_gears = [] 

            if c == "*":
                print(colored(c, "yellow"), end="")
            elif not c.isnumeric():
                if c is not ".":
                    print(colored(c, "blue"), end="")
                else:
                    print(c, end="")

        print()

    ratios = 0
    for nums in gears.values():
        if len(nums) == 2:
            ratios += nums.pop() * nums.pop()


    print("part1", sum(parts))
    print("part2", ratios)


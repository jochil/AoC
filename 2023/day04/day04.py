with open("input") as f:
    r = 0
    lines = [line.strip() for line in f.readlines()]
    instances = [1] * len(lines)
    for i, line in enumerate(lines):
        win, yours = line.split(":")[1].split("|")
        win = [n.strip() for n in win.split(" ") if n != ""]
        yours = [n.strip() for n in yours.split(" ") if n != ""]

        matches = set(win) & set(yours)

        for j in range(len(matches)):
            instances[i+j+1] += instances[i] 

        if len(matches) > 0:
            r += pow(2, len(matches)-1)

    print("part1",r)
    print("part2", sum(instances))

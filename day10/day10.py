x = [1]
with open("input", "r") as f:
    for line in f.readlines():
        inst = line.strip()

        x.append(x[-1])
        if inst.startswith("addx"):
            x.append(x[-1] + int(inst[5:]))

    print("signal strength part 1:", sum([x[i-1] * i for i in range(20, 221, 40)]))

    for r in range(0, 6):
        for c in range(0, 40):
            cycle = c + (r * 40)
            if x[cycle] in [c-1, c, c+1]:
                print("#", end="")
            else:
                print(".", end="")
        print()

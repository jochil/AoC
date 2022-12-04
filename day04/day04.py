inside = lambda a1,a2,b1,b2: (a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2)
overlap = lambda a1,a2,b1,b2: len(set(range(a1, a2+1)) & set(range(b1, b2+1))) > 0

with open("input", "r") as f:
    rows = [list(map(int, line.strip().replace("-",",").split(","))) for line in f.readlines()]
    print("total part 1:", sum([inside(*row) for row in rows]))
    print("total part 2:", sum([overlap(*row) for row in rows]))


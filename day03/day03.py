diff_lower=ord("a")-1
diff_upper=ord("A")-27

priority = lambda c: ord(c) - diff_lower if c.islower() else ord(c) - diff_upper
scan_block = lambda b: priority((set(b[0]) & set(b[1]) & set(b[2])).pop())

def scan_backback(line):
    middle = int(len(line)/2)
    left, right = set(line[:middle]), set(line[middle:])
    return priority((left & right).pop()) 

with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    blocks = [lines[i:i+3] for i in range(0, len(lines), 3)]

    print("total priority part 1:", sum(map(scan_backback, lines)))
    print("total priority part 2:", sum(map(scan_block, blocks)))

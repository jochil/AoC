import re

re_read = r"^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$"

# just for the example input
def draw():
    ys = signal_map.keys()
    for y in range(min(ys), max(ys)+1):
        print(str(y).rjust(5, " "), end="")
        row = expand_ranges(y)
        for x in range(-10, 30):
            c = "."
            if x in row:
                c = "#"
            if (x,y) in sb_map:
                c = sb_map[(x,y)]
            print(c, end="")
        print()

def expand_ranges(y):
    result = set()
    for s, e in signal_map[y].items():
        for x in range(s, e+1):
            # count excluding sensor and beacons
            if (x,y) not in sb_map:
                result.add(x)
    return result

def find_beacon(limit):
    for y in range(0, limit+1):
        for s, e in signal_map[y].items():
            # check if a range overlaps with 0 and ends before the limit
            # if so, its a gap in the signal
            if s < 0 and e > 0 and e < limit+1:
                return (e+1) * 4000000 + y
    
def merge(x1, x2, ranges):
    ignore = False
    for s, e in ranges.copy().items():
        # inside an existing range 
        if x1 >= s and x2 <=e:
            ignore = True
            break
        # check different scenarios like overlapping (left, right, complete)
        # or being close to each other
        elif (x1 < s and x2 <= e and x2 >= s) \
                or (x1 >= s and x1 <= e and x2 > e) \
                or (x1 < s and x2 > e) \
                or x1 == e+1 \
                or x2 == s-1:
            x1, x2 = min(x1, s), max(x2, e)
            del ranges[s]
    if ignore == False:
        ranges[x1] = x2
    return ranges


with open("input", "r") as f:
    sb_map = {}
    signal_map = {}

    for match in re.finditer(re_read, f.read(), re.MULTILINE):
        sx, sy, bx, by = [int(i) for i in match.groups()]

        # save beacon / sensor coordinates
        sb_map[(sx,sy)] = "S" 
        sb_map[(bx,by)] = "B" 

        dist = abs(sx-bx) + abs(sy-by)

        for dy in range(-dist, dist+1):
            w = dist-abs(dy)
            y = sy+dy
            x1 = sx-w
            x2 = sx+w

            # create new dict for range or create a new one
            signal_map[y] = merge(x1, x2, signal_map[y]) if y in signal_map else {x1: x2}

    #draw()
    #print("part 1", len(scan_row(10)))
    #print("part 2", find_beacon(20))
    print("part 1", len(expand_ranges(2000000)))
    print("part 2", find_beacon(4000000))



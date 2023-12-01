def view_line(h, line):
    count = 0
    for e in line:
        count +=1
        if e >= h:
            break
    return count

with open("input", "r") as f:
    grid = [[int(c) for c in list(line.strip())] for line in f.readlines()]

    h = len(grid)
    w = len(grid[0])

    visible = 2*h + 2*w - 4 
    max_view = 0

    for y in range(1,h -1):
        for x in range(1, w-1):
            c = grid[y][x]
            l = grid[y][0:x]
            r = grid[y][x+1:]
            t = [r[x] for r in grid[0:y]]
            b = [r[x] for r in grid[y+1:]]

            visible += max(l) < c or max(r) < c or max(t) < c or max(b) < c

            view = view_line(c, r) * view_line(c, l[::-1]) * view_line(c, b) * view_line(c, t[::-1])
            max_view = view if view > max_view else max_view

    print("visible trees", visible)
    print("max view", max_view)


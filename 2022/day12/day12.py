from collections import defaultdict, deque

def explore(start_points):
    dist = defaultdict(lambda:9999)
    q = deque(start_points)

    for x,y in q:
        dist[x,y] = 0

    while len(q) > 0:
        cx, cy = q.popleft()
        if (cx, cy) == (ex, ey):
            return (dist[ex,ey])
    
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = cx + dx, cy + dy
            if nx in range(w) and ny in range(h):
                if grid[cy][cx] >= grid[ny][nx] - 1:
                    new_dist = dist[cx,cy] + 1
                    if new_dist < dist[nx,ny]:
                        q.append((nx, ny))
                        dist[nx,ny] = new_dist

with open("input", "r") as f:
    gs = [list(line) for line in f.read().splitlines()]
    h = len(gs)
    w = len(gs[0])

    find = lambda c: [(x,y) for x in range(w) for y in range(h) if gs[y][x] == c]

    sx,sy = find("S")[0]
    ex,ey = find("E")[0]
    gs[sy][sx] = "a"
    gs[ey][ex] = "z"

    grid = [[ord(c) - ord('a') for c in row] for row in gs]

    print("part 1:", explore([(sx,sy)]))

    a = find("a")
    print("part 2:", explore(a))
    



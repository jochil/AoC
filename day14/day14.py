import copy

def draw(rocks, blocked, limit_y, bottom):
    xs = [pos[0] for pos in blocked]
    ys = [pos[1] for pos in blocked]
    for y in range(min(ys), max(ys)+3):
        for x in range(min(xs)-5, max(xs)+5):
            if y == limit_y and bottom:
                print("#", end="")
            elif y > limit_y:
                print("-", end="")
            elif (x,y) in rocks.keys():
                print("#", end="")
            elif (x,y) in blocked.keys():
                print("o", end="")
            else:
                print(".", end="")
        print()

    
def simulate(rocks, limit_y, bottom=False):
    blocked = copy.deepcopy(rocks)
    absyss = False
    stucked = False
    while absyss == False and stucked == False:
        # spawn new sand
        sx, sy = (500, 0)
        while True:
            moved = False
            for dx,dy in [(0,1), (-1,1), (1,1)]:
                nx, ny = sx+dx, sy+dy

                # part 2: sand hit bottom
                if ny == limit_y and bottom:
                    break
                if (nx,ny) not in blocked.keys():
                    if ny >= limit_y :
                        absyss = True
                        break
                    else:
                        sx,sy = nx,ny
                        moved = True
                        break

            if absyss == True:
                break

            # sand came to rest
            if moved == False:
                blocked[(sx,sy)] = None
                # part 2: entry point is blocked 
                if sx == 500 and sy == 0:
                    stucked = True
                break

    draw(rocks, blocked, limit_y, bottom)
    return len(blocked) - len(rocks)

with open("input", "r") as f:
    paths = [[[ int(c) for c in point.strip().split(",")] for point in line.split(" -> ")] for line in f.readlines()]
    rocks = {} 
    max_y = 0
    for path in paths:
        for i in range(len(path)-1):
            cx, cy = path[i]
            nx, ny = path[i+1]

            for x in range(min(cx,nx), max(cx,nx)+1):
                for y in range(min(cy,ny),max(cy,ny)+1):
                    rocks[(x,y)] = None
                    if y > max_y: max_y = y

    print("part 1:", simulate(rocks, max_y))
    print("part 2:", simulate(rocks, max_y+2, True))


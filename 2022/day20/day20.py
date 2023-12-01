from collections import deque

def mix(lines, times, factor):
    # store the original position too 
    n = [(i, int(line)*factor) for i, line in enumerate(lines)]
    q = deque(n)
    for _ in range(times):
        p = 0
        while p < len(n):
            # find next one to move, by 
            # checking the left element in queue
            if q[0][0] == p:
                i, v = q.popleft()
                q.insert(v % len(q), (i,v))
                p += 1
            # rotate until the left element 
            # in queue is the next one to move
            else:
                q.rotate(-1)

    # find index of 0
    z = [i for i,v in enumerate(q) if v[1] == 0][0]
    return sum([q[(i+z) % len(n)][1] for i in [1000,2000,3000]])

with open("input") as f:
    lines = f.read().splitlines()
    print("part 1:", mix(lines, 1, 1))
    print("part 2:", mix(lines, 10, 811589153))


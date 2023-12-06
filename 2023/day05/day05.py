import threading
import queue

def find_location(seed):
    curr = seed
    for step in maps:
        for dst, src, rng in maps[step]:
            if curr < src or curr >= src+rng:
                continue
            else:
                offset = curr - src
                curr = dst + offset
                break
    return curr


with open("input") as f:
    content = f.read()

blocks = content.split("\n\n")
seeds = []
maps = {}
for i, block in enumerate(blocks):
    if i == 0:
        seeds = [int(s) for s in block[7:].strip().split(" ")]
    else:
        lines = [line for j, line in enumerate(block.split("\n")) if j > 0]
        maps[i] = [list(map(int, line.strip().split(" "))) for line in lines if line != ""]

def worker():
    while True:
        start, rng = q.get()
        print("working on", start, rng)
        for seed in range(start,start+rng):
            locations.append(find_location(seed))
        print("done with", start, rng)
        q.task_done()

print("part1", min([find_location(seed) for seed in seeds]))

q = queue.Queue()
for _ in range(0, 14):
    threading.Thread(target=worker, daemon=True).start()

locations = []
for i in range(0, len(seeds), 2):
    start, rng = seeds[i:i+2]

    size = 1000000
    parts, _ = divmod(rng, size)
    for j in range(0, parts+1):
        s = start + (j * size)
        r = size if s + size < start+rng else start+rng-s
        q.put([s, r])

q.join()
print("part2", min(locations))

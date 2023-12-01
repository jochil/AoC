block_sums = []
with open("input", "r") as f:
    for block in f.read().split("\n\n"):
        block_sums.append(sum([int(line) for line in block.split()]))

block_sums.sort(reverse=True)
print("top1", block_sums[0])
print("top3", sum(block_sums[:3]))

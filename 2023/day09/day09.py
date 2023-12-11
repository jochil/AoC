scans = []
with open("input_example1") as f:
    scans = [list(map(int, line.split())) for line in f.readlines()]

predictions_future = []
predictions_past = []
for scan in scans:
    steps = [scan]
    curr_step = scan
    while True:
        next_step = []
        for i in range(0, len(curr_step) -1):
            a = curr_step[i]
            b = curr_step[i+1]
            d = b - a
            next_step.append(d)
        steps.append(next_step)

        # stop if the step contains only zeros
        if  next_step.count(0) == len(next_step):
            break
        curr_step = next_step

    # predict next value
    future = 0
    past = 0
    for i in range(len(steps)-2, -1, -1):
        future = steps[i][-1] + future
        past = steps[i][0] - past
    predictions_future.append(future)
    predictions_past.append(past)

print("part1", sum(predictions_future))
print("part2", sum(predictions_past))


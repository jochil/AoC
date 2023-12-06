from functools import reduce

def test(races):
    wins = [0] * len(races)
    i = 0
    for time, dist in races:
        for pressed in range(0, time+1):
            speed = pressed
            time_to_move = time - pressed
            travel = speed * time_to_move
            if travel > dist:
                wins[i]+=1
        i += 1
    return wins

races_p1 = []
races_p2 = []
with open("input") as f:
    lines = f.readlines()

    times = [int(time.strip()) for time in lines[0].split(":")[1].strip().split(" ") if time != ""]
    distances = [int(dist.strip()) for dist in lines[1].split(":")[1].strip().split(" ") if dist != ""]
    races_p1= list(zip(times, distances))

    time = int(reduce(lambda x,y: f"{x}{y}", times))
    distance = int(reduce(lambda x,y: f"{x}{y}", distances))
    races_p2.append((time, distance))

wins_p1 = test(races_p1)
wins_p2 = test(races_p2)
print("part1", reduce(lambda x, y: x*y, wins_p1))
print("part2", wins_p2[0])


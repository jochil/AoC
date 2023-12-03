with open("input") as f:
    valid_games = [] 
    powers = []
    for line in f.readlines():
        game, colors = line.split(":", 2)
        id = int(game[4:])
        showed = {
                "blue": [],
                "red":[],
                "green": []
                }
        for rounds in colors.split(";"):
            for colors in rounds.split(","):
                n, c = colors.strip().split(" ", 2)
                showed[c].append(int(n))

        b = max(showed["blue"])
        g = max(showed["green"])
        r = max(showed["red"])

        if b <= 14 and g <= 13 and r <= 12:
            valid_games.append(id)

        powers.append(b*g*r)

    print("part1", sum(valid_games))
    print("part2", sum(powers))



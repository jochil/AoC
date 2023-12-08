import functools

def find_type(cards):
    counts = {}
    for card in cards:
        if card not in counts:
            counts[card] = 0
        counts[card]+=1

    # five of a kind
    if len(counts) == 1:
        return 7

    if len(counts) == 2:
        # four of a kind
        if 4 in counts.values():
            return 6
        # full house
        if 3 in counts.values():
            return 5

    if len(counts) == 3:
        # three of a kind
        if 3 in counts.values():
            return 4
        # two pairs
        else:
            return 3

    # one pair
    if len(counts) == 4:
        return 2

    # high card
    return 1

def optimize(cards):
    type_org = find_type(cards)
    for r in ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]:
        type_new = find_type(cards.replace("J", r))
        if type_new > type_org:
            type_org = type_new
    return type_org

def values_p1(card):
    return int(card.replace("A", "14")\
        .replace("K", "13") \
        .replace("Q", "12") \
        .replace("J", "11") \
        .replace("T", "10"))

def values_p2(card):
    return int(card.replace("A", "14")\
        .replace("K", "13") \
        .replace("Q", "12") \
        .replace("J", "1") \
        .replace("T", "10"))

def cmp_games(gameA, gameB, type_func, value_func):
    cardsA, _ = gameA.split(" ")
    cardsB, _= gameB.split(" ")
    typeA = type_func(cardsA)
    typeB = type_func(cardsB)

    if typeA > typeB:
        return 1
    elif typeA < typeB:
        return -1

    for i in range(0,5):
        cardA = value_func(cardsA[i])
        cardB = value_func(cardsB[i])
        if cardA < cardB:
            return -1
        elif cardA > cardB:
            return 1

def cmp_games_p1(gameA: str, gameB:str):
    return cmp_games(gameA, gameB, find_type, values_p1)

def cmp_games_p2(gameA: str, gameB:str):
    return cmp_games(gameA, gameB, optimize, values_p2)

with open("input") as f:
    games = [line.strip() for line in f.readlines()]

games_p1 = sorted(games, key=functools.cmp_to_key(cmp_games_p1))
games_p2 = sorted(games, key=functools.cmp_to_key(cmp_games_p2))
print("part1", sum([(i+1)*int(game[6:]) for i, game in enumerate(games_p1)]))
print("part2", sum([(i+1)*int(game[6:]) for i, game in enumerate(games_p2)]))


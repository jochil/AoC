import os

def part1(input):
    ranges_raw, ingredients = input.split("\n\n")
    result = 0
    good = [tuple(map(int, r.split("-"))) for r in ranges_raw.split("\n")]
            
    for ing in ingredients.split("\n"):
        ing = int(ing)
        for s,e in good:
            if s <= ing <= e:
                result += 1
                break

    return result 


def part2(input):
    ranges_raw, _ = input.split("\n\n")
    good = [tuple(map(int, r.split("-"))) for r in ranges_raw.split("\n")]
    good.sort()
    
    s,e = good.pop(0)
    result = 0
    for sc, ec in good:
        # extend if s is in between current range
        if s <= sc <= e:
            e = max(e, ec)
        else:
            result += e - s + 1
            s, e = sc, ec
    
    result += e - s + 1
    return result


wd = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(wd, "input"), "r") as f:
    all = f.read()
    print("part1:", part1(all))
    print("part2:", part2(all))

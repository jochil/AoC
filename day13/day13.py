from functools import cmp_to_key

def compare(left, right):
    match left, right:
        case int(), int():
            return left - right
        case list(), list():
            for l, r in zip(left, right):
                res = compare(l, r)
                if res != 0:
                    return res
            return compare(len(left), len(right))
        case int(), list():
            return compare([left], right)
        case list(), int():
            return compare(left, [right])


with open("input") as f:
    packets = [eval(line) for line in f.read().splitlines() if len(line) != 0]

    right_order = []
    for i in range(0, len(packets), 2):
        left = packets[i]
        right = packets[i+1]
        if compare(left, right) <= 0:
            right_order.append(i//2 + 1) 

    print("part 1:", sum(right_order))

    divider = [[[2]], [[6]]]
    packets.extend(divider)
    sorted_packets = sorted(packets, key=cmp_to_key(compare))
    print("part 2:", (sorted_packets.index(divider[0]) + 1) * (sorted_packets.index(divider[1]) + 1))




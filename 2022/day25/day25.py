def from_snafu(s):
    dec = 0
    for i, c in enumerate(s[::-1]):
        pos = 5 ** i
        f = 0
        match c:
            case "-":
                f = -1
            case "=":
                f = -2
            case _:
                f = int(c)
        dec += pos * f
    return dec

def to_snafu(dec):
    snafu = ""
    q = dec
    while q > 0:
        q, m = divmod(q+2, 5)
        snafu += '=-012'[m]
    return snafu[::-1]
    
with open("input", "r") as f:
    snafus = f.read().splitlines()
    print("part 1:", to_snafu(sum([from_snafu(s) for s in snafus])))

import math

class Monkey():
    def __init__(self, ident, items, test, true, false, op):
        self.ident = ident
        self.items = items
        self.test = test
        self.true = true
        self.false = false
        self.op =  lambda old: eval(op)
        self.count = 0

    def inspect(self, lcm=0, worry_divisor=3):
        while len(self.items) > 0:
            self.count += 1
            item = self.items.pop(0)
            worry = self.op(item) // worry_divisor 
            if lcm != 0:
                worry %= lcm
            if worry % self.test == 0:
                monkies[self.true].items.append(worry)
            else:
                monkies[self.false].items.append(worry)


def load():
    with open("input", "r") as f:
        lines = f.read().splitlines()
        monkies = []
        for i in range(0, len(lines), 7):
            items = [int(item) for item in lines[i+1][17:].split(", ")]
            op = lines[i+2][19:]
            test = int(lines[i+3][21:])
            true = int(lines[i+4][29:])
            false = int(lines[i+5][29:])

            monkies.append(Monkey(len(monkies), items, test, true, false, op))
        return monkies

monkey_business = lambda: math.prod(sorted([m.count for m in monkies], reverse=True)[:2]) 

# part 1
monkies = load()
for r in range(0, 20):
    for m in monkies:
        m.inspect(0)
print("monkey business part 1:", monkey_business())

# part 2
monkies = load()
lcm = math.prod([m.test for m in monkies])
for r in range(0, 10000):
    for m in monkies:
        m.inspect(lcm, 1)
print("monkey business part 2:", monkey_business())

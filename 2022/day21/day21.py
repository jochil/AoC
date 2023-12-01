from collections import deque
import sympy

def read_input(part2=False):
    numbers = {}
    q = deque([])
    with open("input", "r") as f:
        for line in f.read().splitlines():
            name, action = line.split(": ")
            if action.isdigit():
                numbers[name] = int(action)
            else:
                op1, op, op2 = action.split(" ")
                # replace root operation we can solve it against 0 
                if part2 and name == "root":
                    op = "-" 
                q.append((name, op1, op2, op))
    return numbers, q

def solve_for(a, n, q):
    while q and a not in n:
        name, op1, op2, op = q.pop()
        if op1 in n and op2 in n.keys():
            n[name] = int(eval(f"{n[op1]}{op}{n[op2]}"))
        else:
            q.appendleft((name, op1, op2, op))
    return n[a]

def build_expression(n, q):
    result = "root"
    while q:
        name, op1, op2, op = q.pop()
        if name in result:
            result = result.replace(name, f"({op1}{op}{op2})")
        else:
            q.appendleft((name, op1, op2, op))
    for k,v in n.items():
        result = result.replace(k, str(v))
    return result

numbers, q = read_input()
print("part 1:", solve_for("root", numbers, q))

numbers, q = read_input(True)
numbers["humn"] = "x"
print("part 2:", sympy.solve(build_expression(numbers, q))[0])

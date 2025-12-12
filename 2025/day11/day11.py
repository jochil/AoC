import os
import networkx as nx

def part1(lines):
    g = nx.DiGraph()
    for line in lines:
        device, connections = line.split(":")
        for c in connections.split():
            g.add_edge(device, c.strip())
    paths = list(nx.all_simple_paths(g, source="you", target="out"))
    return len(paths)
        

def part2(lines):
    pass
                        

wd = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(wd, "input_example1"), "r") as f:
    print("part1:", part1(f.readlines()))
with open(os.path.join(wd, "input_example2"), "r") as f:
    print("part2:", part2(f.readlines()))

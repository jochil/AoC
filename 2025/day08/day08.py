import os
import math
import networkx as nx
from itertools import combinations

def calc_distances(boxes):
    distances = [] 
    pairs = combinations(boxes, 2)
    for box_a, box_b in pairs:
        distances.append((math.dist(box_a, box_b), box_a, box_b))
    return sorted(distances)


def part1(distances, limit):
    g = nx.Graph()
    for distance, box_a, box_b in distances[:limit]:
        g.add_edge(box_a, box_b)

    circuit_sizes = sorted([len(c) for c in nx.connected_components(g)], reverse=True)
    return math.prod(circuit_sizes[:3])


def part2(boxes, distances):
    g = nx.Graph()
    g.add_nodes_from(boxes)
    for distance, box_a, box_b in distances:
        g.add_edge(box_a, box_b)
        if nx.is_connected(g):
            return box_a[0] * box_b[0]

                        
wd = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(wd, "input_example1"), "r") as f:
    boxes = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]
    distances = calc_distances(boxes)

    print("part1:", part1(distances, 10))
    print("part2:", part2(boxes, distances))

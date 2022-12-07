class Node:
    def __init__(self, name, parent, size):
        self.name = name 
        self.size = size 
        self.children = {}
        self.parent = parent

    def add_child(self, node):
        # just overwrite existing nodes with new ones
        self.children[node.name] = node

    def is_dir(self):
        return self.size == 0

    def calc_size(self):
        return self.size + sum([child.calc_size() for child in self.children.values()])

    def filter(self, filter_func):
        result = [self] if filter_func(self) else []
        for child in self.children.values():
            result.extend(child.filter(filter_func))
        return result

pointer = root = Node("/", None, 0) 
total_size = 70000000
needed_size = 30000000

with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    for line in lines:
        assert pointer 
        # command mode
        if line.startswith("$"):
            # cd command
            if line.startswith("$ cd"):
                if line[5:] == "/":
                    pointer = root
                elif line[5:] == "..":
                    pointer = pointer.parent
                else:
                    node = Node(line[5:], pointer, 0)
                    pointer.add_child(node)
                    pointer = node
            # ls command
            elif line == "$ ls":
                pass
        # listing directory
        else:
            size, name = (0, line[4:]) if line.startswith("dir") else line.split(" ")
            pointer.add_child(Node(name, pointer, int(size)))
            
root_size = root.calc_size()
unused_size = total_size - root_size
missing_size = needed_size - unused_size

filter_func1 = lambda node: node.calc_size() <= 100000 and node.is_dir()
print("part 1", sum([node.calc_size() for node in root.filter(filter_func1)]))

filter_func2 = lambda node: node.calc_size() >= missing_size and node.is_dir()
print("part 2", min([node.calc_size() for node in root.filter(filter_func2)]))

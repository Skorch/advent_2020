import advent_io as io
import re
import networkx as nx

G = nx.DiGraph()

input_file = "day7.input"

inner_bag_re = r'(?P<qty>\d+) (?P<col>(\D)+) bag'

def parse_input_line(line):
    # print(line)
    l1 = line.replace('.','').split("bags contain ")
    outer = l1[0].strip()
    # print(f"{outer}")

    inner_parse = lambda match: {"color": match.group("col").strip(), "qty": int(match.group("qty"))}
    inner_bags = [inner_parse(match) for match in re.finditer(inner_bag_re, l1[1])]

    return (outer, inner_bags)

for line in io.read_input(input_file):
    outer, inner = parse_input_line(line)
    G.add_node(outer)
    for bag in inner:

        color = bag["color"]
        qty = bag["qty"]
        G.add_node(color)
        G.add_edge(color, outer, weight=qty )

    # print(f"outer: {outer} inner: {inner}")

print(f"nodes {G.number_of_nodes()} edges {G.number_of_edges()}")

def x(node, bags = set()):
    if node not in bags:
        # print(f"adding {node}")
        bags.add(node)
        connected = G[node]
        if connected:
            for bag in connected:
                # print(f"getting edges for {bag}")
                bags |= x(bag, bags)
    # print(f"returning {bags}")
    return bags

node = 'shiny gold'
result = x(node)
result.remove(node)
# print(f"{list(result)}")
print(f"{len(list(result))}")

# print(list(nx.dfs_edges(G, source="shiny gold")))

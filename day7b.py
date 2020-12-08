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
        G.add_edge(outer, color, weight=qty )

    # print(f"outer: {outer} inner: {inner}")

print(f"nodes {G.number_of_nodes()} edges {G.number_of_edges()}")

def x(node):

    connected = G[node]
        
    if connected:

        qty = 1

        for bag in connected:
            edge = G.edges[node, bag]
            inner_bag = x(bag)
            print(f"getting edges for {bag} weight {edge['weight']} = {edge['weight'] * inner_bag}")
            qty += (edge["weight"] * inner_bag)

        return qty
    else:
        return 1


node = 'shiny gold'
result = x(node) - 1
print(result)

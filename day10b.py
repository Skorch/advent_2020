import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

data = np.array(np.sort(np.loadtxt('day10.input', dtype=int)))

data = np.insert(data, values=[0], obj=[0])
data = np.insert(data, values=[data.max() + 3], obj=[-1])
data = np.sort(data)
def build_graph(input):
    g = nx.DiGraph()
    paths = {}

    for ix, val in enumerate(input):
        options = []
        cur_path_count = paths.get(val, 1)

        for next_ix in range(ix+1, len(input)):
            next_val = input[next_ix]
            next_path_count = paths.get(next_val, 0)
            print(f"setting node {next_val} ({next_path_count}) from {val} count to {next_path_count + cur_path_count}")
            paths[next_val] = next_path_count+ cur_path_count
            diff = next_val - val
            # print(f"{next_val} - {val} = {diff}")
            if diff <= 3 and diff > 0:
                # print(f"adding edge {val} to {next_val} weight {diff}")
                g.add_edge(val, next_val)
                options.append(next_val)
            else:
                break
        
    print(paths)
    return g

def count_paths(g):

    paths = {}

    for val in nx.topological_sort(g):
        cur_path_count = paths.get(val, 1)
        for next_val in g[val]:
            paths[next_val] = paths.get(next_val, 0)+ cur_path_count
        
    
    return paths



# total_data = np.array(np.meshgrid(data, data)).T.reshape(-1,2)

# g = nx.from_numpy_array(total_data)
G = build_graph(data)
# print(f"nodes {G.number_of_nodes()} edges {G.number_of_edges()}")
# cutoff = len(list(data))

x = count_paths(G)

print(x)

nx.draw_networkx(G, pos=nx.spring_layout(G))
plt.show()


#     print(len(G[x]))
#     for y in G[x]:

#         print(y)
#         # print(nx.dfs_edges(G[x]))





# for path in paths:
#     print(f"{np.array(path)}")


# diff_count = {}

# for ix in range(1, len(data)):
#     diff = data[ix] - data[ix-1]
#     diff_count[diff] = diff_count.get(diff, 1) + 1

# print(f"{(diff_count[1])} {(diff_count[3])} {(diff_count[1]) *(diff_count[3])}")


# print(f"{G[10]}")

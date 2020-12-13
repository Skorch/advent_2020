import advent_io as io

import numpy as np

# shift clockwise (right)
N = 'N'
E = 'E'
S = 'S'
W = 'W'

v = {
    'N': [1, 0],
    'E': [0, 1],
    'S': [-1, 0],
    'W': [0, -1]
}
degree_shift = {
    'N': [E, S, W ],
    'E': [ S, W, N ],
    'S': [ W, N, E ],
    'W': [ N, E, S ] ,
}

# N/S, E/W
direction = E
position = [0,0]
for line in io.read_input('day12.input'):
    op = line[0]
    val = int(line[1:])

    if op == 'F':        
        position = np.add(position, np.multiply(v[direction], val))
    elif op == 'R':
        x = int(val/90) - 1
        direction = degree_shift[direction][int(val/90) - 1]
    elif op == 'L':
        direction = list(reversed(degree_shift[direction]))[(int(val/90) - 1)]
    elif op in v:
        position = np.add(position, np.multiply(v[op], val))
    else:
        raise Exception(f"Op not supported {op}")

print(f'answer: {np.sum(np.abs(position))}')
import advent_io as io

import numpy as np

# shift clockwise (right)
N = 'N'
E = 'E'
S = 'S'
W = 'W'

v = {
    'N': [[1, 0],[0,0]],
    'E': [[0, 1], [0,0]],
    'S': [[0,0], [0, 1]],
    'W': [[0,0], [1, 0]]
}
degree_shift = {
    'N': [E, S, W ],
    'E': [ S, W, N ],
    'S': [ W, N, E ],
    'W': [ N, E, S ] ,
}

# N/S, E/W
direction = E
position = [[0,0], [0,0]]
waypoint = [[1,10],[0,0]]
for line in io.read_input('day12.input'):
    op = line[0]
    val = int(line[1:])

    if op == 'F':        
        position = np.add(position, np.multiply(waypoint, val))
    elif op == 'R':
        waypoint = np.rot90(waypoint, -int(val/90))
    elif op == 'L':
        waypoint = np.rot90(waypoint, x = int(val/90))        
    elif op in v:
        waypoint = np.add(waypoint, np.multiply(v[op], val))
    else:
        raise Exception(f"Op not supported {op}")

ew = abs(position[0][1] - position[1][0])
ns = abs(position[0][0] - position[1][1])
print(f'answer: e/w = {ew} n/s = {ns} = {ew+ns}')
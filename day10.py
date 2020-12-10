import numpy as np

data = np.sort(np.loadtxt('day10.input', dtype=int))

print(np.sort(data))

diff_count = {}

for ix in range(1, len(data)):
    diff = data[ix] - data[ix-1]
    diff_count[diff] = diff_count.get(diff, 1) + 1

print(f"{(diff_count[1])} {(diff_count[3])} {(diff_count[1]) *(diff_count[3])}")

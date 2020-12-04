# From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

# The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

# ..##.........##.........##.........##.........##.........##.......  --->
# #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
# .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
# ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
# .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
# ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
# .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
# .#........#.#........X.#........#.#........#.#........#.#........#
# #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
# #...##....##...##....##...#X....##...##....##...##....##...##....#
# .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
# In this example, traversing the map using this slope would cause you to encounter 7 trees.

# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?

import io

input_file = 'day3.input'

cur_y = 0
d_y = 1
d_x = 3
cur_x = 0
total_trees = 0

with io.open(input_file, 'rt') as f:
    convert_line = lambda line: [True if c == '#' else False for c in line]  
    sled_map = [convert_line(line) for line in f.readlines()]

row_len = len(sled_map[0]) - 1

while cur_y < len(sled_map) - 1:
    cur_y += d_y
    cur_x += d_x

    val = sled_map[cur_y][cur_x % row_len]
    print(f"cur_y: {cur_y} cur_x: {cur_x} {cur_x%row_len} {row_len} val: {val}")

    total_trees += 1 if val else 0

    print(total_trees)

# print(sled_map)
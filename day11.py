import numpy as np
import advent_io as io

encode_seat = lambda s: 0 if s=='L' else np.nan
encode_line = lambda  l: [encode_seat(s) for s in l]
room = np.array([encode_line(l) for l in io.read_input('day11.input')])


adjacent_count = 4

def adjacent_seats(row, col, room):
    max_row = len(room) - 1
    max_col = len(room[row]) - 1
    return [
        room[row - 1, col - 1] if row > 0 and col > 0 else np.nan,
        room[row - 1, col] if row > 0 else np.nan,
        room[row - 1, col + 1] if row > 0 and col < max_col else np.nan,
        room[row, col - 1] if col > 0 else np.nan,
        room[row, col + 1] if col < max_col else np.nan,
        room[row + 1, col - 1] if row < max_row and col > 0 else np.nan,
        room[row + 1, col] if row < max_row else np.nan,
        room[row + 1, col + 1] if row < max_row and col < max_col else np.nan,
    ]

def process_seat(row_ix, col_ix, room):
    row = room[row_ix]
    seat = row[col_ix]
    #if not seat do nothing
    # if seat filled and prev 4 or next 4 are filled, unfill
    # if first seat and next is not filled then fill
    # if last seat and prev is not filled then fill
    # if not first/last and prev/next are not filled then fill
    row_len = len(row)

    adjacent = adjacent_seats(row_ix, col_ix, room)
    taken = np.nansum(adjacent)

    # print(seat)
    if np.isnan(seat):
        # print("seat is nan")
        return seat
    elif seat == 0 and taken == 0:
        return 1
    elif seat == 1 and taken >= 4:
        return 0
    else:
        return seat


def process_row(row_ix, room):
    return [process_seat(row_ix, ix, room) for ix in range(0, len(room[row_ix])) ]

def process_room(room):
    return np.array([process_row(ix, room) for ix in range(0, len(room))])


print("============")
print(room)

x = 0
while True:

    prev_room = room
    room = process_room(room)
    print(x)
    # print(room)

    if np.array_equal(prev_room, room, equal_nan=True):
        print(f"room has not changed and has {np.nansum(room)} seats")
        break

    x += 1
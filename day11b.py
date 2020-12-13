import numpy as np
from numpy.lib.type_check import nan_to_num
from numpy.ma.core import diag
import advent_io as io

encode_seat = lambda s: 0 if s=='L' else np.nan
encode_line = lambda  l: [encode_seat(s) for s in l]
room = np.array([encode_line(l) for l in io.read_input('day11.input')])


adjacent_count = 5

def process_seat(row_ix, col_ix, room):
    row = room[row_ix]
    seat = row[col_ix]
    #if not seat do nothing
    # if seat filled and prev 4 or next 4 are filled, unfill
    # if first seat and next is not filled then fill
    # if last seat and prev is not filled then fill
    # if not first/last and prev/next are not filled then fill
    row_len = len(row)

    adjacent = adjacent_taken(row_ix, col_ix, adjacent_matrix(row_ix, col_ix, room))    
    taken = np.nansum(adjacent)

    # if col_ix == 0:
    #     print(f"({row_ix},{col_ix}) seat: {seat} \nadjacent {adjacent} \ntaken {taken}")
    if np.isnan(seat):
        # print("seat is nan")
        return seat
    elif seat == 0 and taken == 0:
        return 1
    elif seat == 1 and taken >= adjacent_count:
        return 0
    else:
        return seat


def process_row(row_ix, room):
    return [process_seat(row_ix, ix, room) for ix in range(0, len(room[row_ix])) ]

def process_room(room):
    return np.array([process_row(ix, room) for ix in range(0, len(room))])

def adjacent_matrix(row, col, room):

    diag_offset = col - row
    anti_offset = (-room.shape[1] + (row + col) + 1)
    diag = room.diagonal(offset=(col-row))
    anti = np.rot90(room).diagonal(offset=anti_offset)

    return {
        "row": room[row],
        "col": room.T[col],
        # kind of hacky but want to make sure the shape is consistent with the index
        "diag": np.pad(diag, (abs(diag_offset) if diag_offset < 0 else 0, diag_offset if diag_offset > 0 else 0), constant_values=np.nan),
        "anti-diag": np.pad(anti, (anti_offset if anti_offset > 0 else 0, abs(anti_offset) if anti_offset < 0 else 0), constant_values=np.nan)
    }

def adjacent_taken(row, col, adj):
    ar = lambda x: list(x)[0]
    last = lambda x, y: y[x[-1]] if len(x) else np.nan
    first = lambda x, y: y[x[0]] if len(x) else np.nan
    row_vals = adj['row']
    col_vals = adj['col']
    diag_vals = adj['diag']
    anti_vals = adj['anti-diag']
    row_seats = ar(np.where(row_vals >= 0))
    col_seats = ar(np.where(col_vals >= 0))
    diag_seats = ar(np.where(diag_vals >= 0))
    anti_seats = ar(np.where(anti_vals >= 0))

    # if col==0:
    #     print(f"row {row_seats}")
    #     print(np.where(diag_seats < row))
    #     print(diag_seats[np.where(diag_seats < row)])
    #     # print(row_vals[row_seats[np.where(row_seats > col)][0]])
    #     print(f"col {col_seats}")
    #     print(f"diag {diag_seats}")
    #     print(f"anti {anti_seats}")
    
    return np.array([
        [
        last(diag_seats[np.where(diag_seats < row)], diag_vals),
        last(col_seats[np.where(col_seats < row)], col_vals),
        last(anti_seats[np.where(anti_seats < row)], anti_vals),
        ],
        [
        last(row_seats[np.where(row_seats < col)], row_vals),
        np.nan,
        first(row_seats[np.where(row_seats > col)], row_vals),
        ],
        [
        first(anti_seats[np.where(anti_seats > row)], anti_vals),
        first(col_seats[np.where(col_seats > row)], col_vals),
        first(diag_seats[np.where(diag_seats > row)], diag_vals),
        ]
    ]    )


# room = process_room(room)

print("STARTING ========")

print(room)

x = 0
while True:

    prev_room = room.copy()
    room = process_room(room)
    print(x)
    # print(room)

    if np.array_equal(prev_room, room, equal_nan=True):
        print(f"room has not changed and has {np.nansum(room)} seats")
        break

    x += 1
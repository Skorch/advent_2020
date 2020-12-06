import io

input_file = 'day5.input'

total_rows = 128
total_cols = 7

def fetch_row(start, end, code, low_code):

    half = int((end-start) / 2)

    next_start, next_end = (start, start + half) if code[0:1] == low_code else (end - half, end)

    if len(code) > 1:
        return fetch_row(next_start, next_end, code[1:], low_code)
    else:
        return next_start


def process_seat_id(line):
    x1 = fetch_row(0, total_rows, line[:7], "F")
    y1 = fetch_row(0, total_cols, line[7:], "L")
    print(f"row {x1} seat {y1} = {x1*8 + y1}")
    return (x1*8) + y1

with io.open(input_file, 'rt') as f:

    answer = max([process_seat_id(line) for line in f.readlines()])
    print(answer)

import io

input_file = 'day5.input'

total_rows = 128
total_cols = 7


def fetch_row(start, end, code, low_code):

    half = int((end-start) / 2)

    next_start, next_end = (start, start + half) if code[0:1] == low_code else (end - half, end)
    # print(f"code: {code} start {next_start} end {next_end}")

    if len(code) > 1:
        # print(f"code: {code}")
        return fetch_row(next_start, next_end, code[1:], low_code)
    else:
        # print(f"code: {code}")
        return next_start if low_code == code else next_start


def process_seat_id(line):
    x1 = fetch_row(0, total_rows, line[:7], "F")
    y1 = fetch_row(0, total_cols, line[7:], "L")
    # print(f"row {x1} seat {y1} = {x1*8 + y1}")
    return {
        "row": x1,
        "seat": y1,
        "seat_id": (x1*8) + y1
    }

with io.open(input_file, 'rt') as f:


    seat_buffer = []
    for seat_id in sorted([process_seat_id(line.strip()) for line in f.readlines()], key=lambda x: x.get("seat_id")):
        if len(seat_buffer) == 2:

            if seat_buffer[1]["seat_id"] - seat_buffer[0]["seat_id"] > 1:
                print(f"missing seat: between {seat_buffer[0]}, {seat_buffer[1]}")

            seat_buffer.pop(0)


        seat_buffer.append(seat_id)        

        # print(seat_buffer)


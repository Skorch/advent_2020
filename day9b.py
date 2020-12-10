import io
import numpy as np
import day9
input_file = 'day9.input'

check = day9.get_answer() #15353384

data = np.loadtxt(input_file, dtype=int)


start_index = 0

def check_df(data, check):
    for x in range(2, len(data)):
        data_range = data[0:x-1]
        val = data_range.sum()
        print(f"{val} == {check}")
        if val == check:
            return (data_range.min(), data_range.max())
        elif val > check:
            return (None, None)



while True:

    min_value, max_value = check_df(data, check)

    if min_value:
        print(f"found match in {min_value} + {max_value} {min_value + max_value}")
        break

    data = np.delete(data,0)

    if len(data) <= 2:
        raise Exception("doesn't work")

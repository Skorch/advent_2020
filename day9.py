import io

input_file = 'day9.input'

with io.open(input_file, 'rt') as f:

    raw_data = [int(line) for line in f.read().split('\n')]

preable_len = 25
next_line = preable_len

preable = raw_data[0: preable_len]
data = raw_data[preable_len:]

print(preable)
print(data)
data_len = len(raw_data) - preable_len

def check_preamble(preamble, number):
    for item in preamble:
        check = number - item
        if check in preable:
            return True

    return False

def get_answer():

    for x in range(preable_len, len(data)):
        compare = data.pop(0)


        print(f"looking for valid number {compare} in preable {preable}")
        if not check_preamble(preable, compare):
            print(f"nothing found for {compare}")
            return compare

        preable.pop(0)
        preable.append(compare)

if __name__ == "__main__":
    print(get_answer())
import io

def read_input(filename):
    with io.open(filename, 'rt') as f:
        for line in f.readlines():
            yield line.strip()
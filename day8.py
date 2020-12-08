import advent_io as io
import re

input_file = "day8.input"

op_re = r'^(?P<op>\w+) (?P<val>(-|\+)?(\d+))$'

executed = set()

def parse_input_line(line):

    match = re.search(op_re, line)
    return {"operation": match.group("op").strip(), "value": int(match.group("val"))}

def process_op(op, cur_op_index, accumulator):

    op_name = op.get("operation")
    op_value = op.get("value")
    print(f"processing {op_name} {op_value}")
    if op_name == "nop":
        return (cur_op_index + 1, accumulator)
    elif op_name == "acc":
        return (cur_op_index + 1, accumulator + op_value)
    elif op_name == "jmp":
        return (cur_op_index + op_value, accumulator)
    else:
        raise Exception(f"Invalid Op! {op_name}")


ops = [parse_input_line(line) for line in io.read_input(input_file)]

cur_op_index = 0
accumulator = 0
ix = 0
while ix < len(ops):

    op = ops[cur_op_index]
    prev_accumulator = accumulator
    cur_op_index, accumulator = process_op(op, cur_op_index, accumulator)
    
    if cur_op_index in executed:
        print(f"loop detected in {ix} iterations at {cur_op_index}.  accumulator={prev_accumulator}")
        break
    else:
        executed.add(cur_op_index)
    
    ix += 1

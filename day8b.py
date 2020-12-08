from typing import ChainMap
import advent_io as io
import re

input_file = "day8.input"

op_re = r'^(?P<op>\w+) (?P<val>(-|\+)?(\d+))$'

def parse_input_line(line):

    match = re.search(op_re, line)
    return {"operation": match.group("op").strip(), "value": int(match.group("val"))}

def process_op(op_name, op_value, cur_op_index, accumulator):

    # print(f"processing {op_name} {op_value}")
    if op_name == "nop":
        return (cur_op_index + 1, accumulator)
    elif op_name == "acc":
        return (cur_op_index + 1, accumulator + op_value)
    elif op_name == "jmp":
        return (cur_op_index + op_value, accumulator)
    else:
        raise Exception(f"Invalid Op! {op_name}")

changed_indexes = []

def test_code(ops, change_index, change_op):

    executed = set()
    cur_op_index = 0
    accumulator = 0
    last_changable_index = 0

    while cur_op_index < len(ops):

        op = ops[cur_op_index]
        op_name = op.get("operation")
        op_value = op.get("value")

        if cur_op_index == change_index:
            op_name = change_op

        cur_op_index, accumulator = process_op(op_name, op_value, cur_op_index, accumulator)
        
        if cur_op_index in executed:
            print("loop detected")
            return None
        else:
            executed.add(cur_op_index)
        

    return accumulator

fixed = False
changable_index = None
accumulator = 0

ops = [parse_input_line(line) for line in io.read_input(input_file)]

changes = []
for ix, op in enumerate(ops):
    op_name = op.get("operation")
    if op_name in ['jmp', 'nop']:
        changes.append((ix, 'jmp' if op_name == 'nop' else 'nop'))

for change_index, change_op in changes:
    print(f"trying change {change_op} at {change_index}")
    accumulator = test_code(ops, change_index, change_op)
    if accumulator:
        print(f"program complete.  accumulator={accumulator}")
        break


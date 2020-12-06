import advent_io as io


input_file = "day6.input"

answers = []

group_set = set()
for line in io.read_input(input_file):
    if not line:        
        answers.append(len(group_set))
        group_set.clear()
    else:
        group_set |= set(list(line))

# final answers
answers.append(len(group_set))

print(f"answer: {sum(answers)}")
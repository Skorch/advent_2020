import advent_io as io


input_file = "day6.input"

answers = []

answer_set = []

def parse_answers(answer_group):
    # print(f"answers: {answer_group}")

    group_set = set()
    for ix, answer in enumerate(answer_group):
        if ix:
            group_set &= set(answer)
        else:
            group_set = set(answer)

    return len(group_set)

for line in io.read_input(input_file):
    
    if not line:
        answers.append( parse_answers(answer_set) )
        answer_set = []
    else:
        answer_set.append(list(line))

# final answers
answers.append( parse_answers(answer_set) )

print(f"answer: {sum(answers)}")
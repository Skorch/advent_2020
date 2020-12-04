# Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

# For example, suppose your expense report contained the following:

# 1721
# 979
# 366
# 299
# 675
# 1456
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

# Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?


import io
import itertools

target = 2020

with io.open('day1.csv', 'rt') as f:
    
    numbers_input = f.readlines()
    numbers = set(int(x) for x in numbers_input)

for number1, number2 in itertools.product(numbers, numbers):
    check = target - (number1+number2)

    if check in numbers:
        print(f"answer: {number1*number2*check}")
        break

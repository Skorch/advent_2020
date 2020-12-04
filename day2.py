# our flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

# The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

# Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

# To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

# For example, suppose you have the following list:

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

# [policy]: [pwd]

# policy: [min]-[max] [letter]: [password]

# In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

# How many passwords are valid according to their policies?



import io
import re


target = 2020

regex = r"(\d+)-(\d+) (.): (.+)"

def parse_line(line):
    matches = re.search(regex, line)


    if not matches:
        print(f"No matches for {line}")
        return None
    min_num = int(matches.group(1))
    max_num = int(matches.group(2))
    match_alpha = matches.group(3)
    pwd = matches.group(4)


    return (min_num, max_num, match_alpha, pwd)


def check_pwd(min_num, max_num, match_alpha, pwd):
    total = re.findall(match_alpha, pwd)

    return len(total) >= min_num and len(total) <= max_num

with io.open('day2.input', 'rt') as f:
    

    valid = []

    for min_num, max_num, match_alpha, pwd in [parse_line(line) for line in f.readlines()]:
        # print(f"{min_num}, {max_num}, {match_alpha}, {pwd}")

        total = re.findall(match_alpha, pwd)

        if check_pwd(min_num, max_num, match_alpha, pwd):
            valid.append(pwd)
        else:
            print(f"{pwd} invalid")
        
    print(f"total valid {len(valid)}")
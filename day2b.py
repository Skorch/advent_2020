# While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

# The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

# Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

# Given the same example list from above:

# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
# How many passwords are valid according to the new interpretation of the policies?

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

    pos1 = pwd[min_num-1]
    pos2 = pwd[max_num-1]

    print(f"pos1: {pos1} {(pos1 == match_alpha)} pos2: {pos2} {(pos2 == match_alpha)} result: {(pos1 == match_alpha) ^ (pos2 == match_alpha)}")
    return (pos1 == match_alpha) ^ (pos2 == match_alpha)

with io.open('day2.input', 'rt') as f:
    

    valid = []

    for min_num, max_num, match_alpha, pwd in [parse_line(line) for line in f.readlines()]:
        print(f"{min_num}, {max_num}, {match_alpha}, {pwd}")

        total = re.findall(match_alpha, pwd)

        if check_pwd(min_num, max_num, match_alpha, pwd):
            valid.append(pwd)
        else:
            print(f"{pwd} invalid")
        
    print(f"total valid {len(valid)}")
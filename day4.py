import io
import re

input_file = 'day4.input'

passport_re = r'ecl:(?P<ecl>.+) pid:(?P<pid>.+)'



required_keys = [
'byr',
'iyr',
'eyr',
'hgt',
'hcl',
'ecl',
'pid',
# 'cid'
]

def parse_passport(buffer):

    print(f"buffer:{buffer}")
    passport = {}
    for key,value in [kvp.split(":") for kvp in buffer.split(" ")]:
        passport[key] = value

    print(f"passport: {passport}")


    return passport

def valid_passport(passport):
    for key in required_keys:
        if not passport.get(key):
            return False
    
    return True

passports = []
buffer = ""
with io.open(input_file, 'rt') as f:
    for line in f.readlines():
        print(f"{len(line)} {line}")
        if line == "\n":
            passports.append(parse_passport(buffer))
            buffer = ""
        else:
            buffer += (' ' if buffer else '') + line.strip()

valid = list(filter(valid_passport, passports))

print(len(valid))

import io
import re

input_file = 'day4.input'

passport_re = r'ecl:(?P<ecl>.+) pid:(?P<pid>.+)'

def check_re(regex, input):
    return re.match(regex, input)

def check_number_range(min, max, value):
    return int(value) >= min and int(value) <= max

def check_height(min_cm, max_cm, min_in, max_in, x):
    if 'cm' in x:
        val = int(x.replace("cm", ""))
        return val >= min_cm and val <= max_cm
    elif 'in' in x:
        val = int(x.replace("in", ""))
        return val >= min_in and val <= max_in
    else:
        return False


required_keys = {
    "byr": (lambda x: check_number_range(1920, 2002, x)),
    "iyr": (lambda x: check_number_range(2010, 2020, x)),
    "eyr": (lambda x: check_number_range(2020, 2030, x)),
    "hgt": (lambda x: check_height(150, 193, 59, 76, x)),
    "hcl": (lambda x: check_re(r"^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$", x)),
    "ecl": (lambda x: check_re(r"^(?:amb|blu|brn|gry|grn|hzl|oth)$", x)),
    "pid": (lambda x: check_re(r"^\d{9}$", x)),
}

def parse_passport(buffer):

    print(f"buffer:{buffer}")
    passport = {}
    for key,value in [kvp.split(":") for kvp in buffer.split(" ")]:
        passport[key] = value

    print(f"passport: {passport}")


    return passport

def valid_passport(passport):
    for key in required_keys:
        valid = required_keys[key]
        value = passport.get(key)
        if not value:
            return False
        if not valid(value):
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

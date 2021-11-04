# AoC 2020 - Day 4

# Stargazer

# ---------------------
#
# Status:
# Part 1 - Code validated and answer delivered
# Part 2 - Code validated and answer delivered
# 
# --------------------

import argparse, sys, string, re

parser = argparse.ArgumentParser("Select passport file to check")

parser.add_argument("-pf","--passport_file", 
                    type=str, 
                    default = "2020")

args = parser.parse_args()

if args.passport_file == "test":
    all_passport = ""

    f = open("test_data_part2.txt", "r")

    for lines in f.readlines():
        all_passport += lines

    f.close()

elif args.passport_file == "puzzle_input":
    all_passport = ""

    f = open("passports.txt", "r")

    for lines in f.readlines():
        all_passport += lines

    f.close()

else:
    print ("No passport file selected. Program terminated")
    sys.exit(1)


passports =  []
d_passports = {}

mustHaveFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optField = "cid"

def check_fields(key1):
    return len(d_passports[key1].keys()) == 8 or len(d_passports[key1].keys()) == 7 and "cid" not in d_passports[key1].keys() 

def check_yr(key1, key2, start, end):
    return len(d_passports[key1][key2]) == 4 and int(d_passports[key1][key2]) >= start and int(d_passports[key1][key2]) <= end

def check_height(key1):
    if d_passports[key1]["hgt"][-2:] == "cm":
        return int(d_passports[key1]["hgt"][:-2]) >= 150 and int(d_passports[key1]["hgt"][:-2]) <=193
    elif d_passports[key1]["hgt"][-2:] == "in":
        return int(d_passports[key1]["hgt"][:-2]) >= 59 and int(d_passports[key1]["hgt"][:-2]) <=76
    else:
        return False

def check_hcl(key1):
    regex = "^#[0-9a-f]{6}"
    if re.match(regex, str(d_passports[key1]["hcl"])):
        return True
    else:
        return False

def check_ecl(key1):
    return str(d_passports[key1]["ecl"]) in ["amb","blu","brn","gry","grn","hzl","oth"]

def check_pid(key1):
    return len(d_passports[key1]["pid"]) == 9

validPassports = 0

one_passport = all_passport.split("\n")

while len(one_passport) > 0:
    i = one_passport.index("")
    onePass = " ".join(one_passport[0:i])
    passports.append(onePass)
    onePass = ""
    del one_passport[0:i+1]

for i in range(len(passports)):
    key = "Passport"+str(i)
    d_passports[key] = {}
    pairs_list = passports[i].split(" ")
    for elm in pairs_list:
        key_elm, value_elm = elm.split(":")
        d_passports[key][key_elm] = value_elm

boolean = False

for key1 in d_passports.keys():
    if check_fields(key1) and check_yr(key1, "byr", 1920, 2002) and check_yr(key1, "iyr", 2010, 2020) and check_yr(key1, "eyr", 2020, 2030) and check_height(key1) and check_hcl(key1) and check_ecl(key1) and check_pid(key1):
        validPassports += 1

    """
    # Also correc to do the following

    if not check_fields(key1):
        continue
    else:
        if not check_yr(key1, "byr", 1920, 2002):
            continue
        else:
            if not check_yr(key1, "iyr", 2010, 2020):
                continue
            else:
                if not check_yr(key1, "eyr", 2020, 2030):
                    continue
                else:
                    if not check_height(key1):
                        continue
                    else:
                        if not check_hcl(key1):
                            continue
                        else:
                            if not check_ecl(key1):
                                continue
                            else:
                                if not check_pid(key1):
                                    continue
                                else:
                                    validPassports +=1
    """

print ("Valid passports: %i" % validPassports)



"""
# Part 1

import argparse, sys

parser = argparse.ArgumentParser("Select passport file to check")

parser.add_argument("-pf","--passport_file", 
                    type=str, 
                    default = "2020")

args = parser.parse_args()


if args.passport_file == "test":
    all_passport = ""

    f = open("test_data_part1.txt", "r")

    for lines in f.readlines():
        all_passport += lines

    f.close()


elif args.passport_file == "puzzle_input":
    all_passport = ""

    f = open("passports.txt", "r")

    for lines in f.readlines():
        all_passport += lines

    f.close()

else:
    print ("No passport file selected. Program terminated")
    sys.exit(1)



passports =  []
d_passports = {}
mustHaveFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optField = "cid"
validPassports = 0

one_passport = all_passport.split("\n")

while len(one_passport) > 0:
    i = one_passport.index("")
    onePass = " ".join(one_passport[0:i])
    passports.append(onePass)
    onePass = ""
    del one_passport[0:i+1]

for i in range(len(passports)):
    key = "Passport"+str(i)
    d_passports[key] = {}
    pairs_list = passports[i].split(" ")
    for elm in pairs_list:
        key_elm, value_elm = elm.split(":")
        d_passports[key][key_elm] = value_elm


for elm in d_passports.keys():
    if len(d_passports[elm].keys()) == 8:
        validPassports += 1
    else:
        if optField not in d_passports[elm].keys() and len(d_passports[elm].keys()) == 7:
            validPassports += 1
        else:
            continue

print ("Valid passports: %i" % validPassports)


"""

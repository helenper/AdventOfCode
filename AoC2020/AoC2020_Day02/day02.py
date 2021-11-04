# AoC 2020 - Day 2

# Stargazer


# --------------------
#
# Status: 
# Part 1
# Part 2
#
# -------------------


import argparse, sys

parser = argparse.ArgumentParser("Select list of passwords to run pasword check on.")

parser.add_argument("-l", "--list",
                    type=str,
                    default=2020)

args = parser.parse_args()

if args.list == "test":
    l = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

elif args.list == "puzzle_input":
    l = []

    f = open("passwords_day02.txt", "r")

    for lines in f.readlines():
        l.append(lines.replace("\n", ""))

    f.close()

else: 
    print "No valid input list selected. Program is terminated"
    sys.exit(1)



def validPwdCheck(pos1, pos2, letter, pwd):
    global validPwdCount
    
    if (pwd[int(pos1)-1] == letter and pwd[int(pos2)-1] != letter) or (pwd[int(pos1)-1] != letter and pwd[int(pos2)-1] == letter) :
            validPwdCount += 1


validPwdCount = 0


for elm in l: 
    numbs, letter_val, pwd = elm.split(" ")
    pos1, pos2 = numbs.replace("-", " ").split(" ")
    letter = letter_val.replace(":", "")

    validPwdCheck(pos1, pos2, letter, pwd)


print "------------------"
print "" 
print "Number of correct passwords and AoC answer is: %i." % validPwdCount
print ""
print "-----------------"



"""
#Part 1


import argparse, sys

parser = argparse.ArgumentParser("Select list of passwords to run pasword check on.")

parser.add_argument("-l", "--list",
                    type=str,
                    default=2020)

args = parser.parse_args()

if args.list == "test":
    l = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

elif args.list == "puzzle_input":
    l = []

    f = open("passwords_day02.txt", "r")

    for lines in f.readlines():
        l.append(lines.replace("\n", ""))

    f.close()

else: 
    print "No valid input list selected. Program is terminated"
    sys.exit(1)



def validPwdCheck(min_val, max_val, letter, pwd):
    global validPwdCount

    instanceOfLetter = pwd.count(letter) 
    
    if int(min_val) <= instanceOfLetter <= int(max_val):
            validPwdCount += 1


validPwdCount = 0


for elm in l: 
    numbs, letter_val, pwd = elm.split(" ")
    min_val, max_val = numbs.replace("-", " ").split(" ")
    letter = letter_val.replace(":", "")

    validPwdCheck(min_val, max_val, letter, pwd)


print "------------------"
print "" 
print "Number of correct passwords and AoC answer is: %i." % validPwdCount
print ""
print "-----------------"

"""




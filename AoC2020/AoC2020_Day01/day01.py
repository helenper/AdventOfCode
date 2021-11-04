# AoC 2020 - Day 1

# Stargazer

# ----------------------
#
# Status: 
# Part 1 is validated and answer delivered
# Part 2 is started
# 
# ---------------------

import argparse, sys

parser = argparse.ArgumentParser("Select what list to run code for")

parser.add_argument("-l", "--list", 
                    type=int, 
                    default=2020)

args = parser.parse_args()

if args.list == 1:
    l = [1721, 979, 366, 299, 675, 1456]

elif args.list == 2:
    l = []

    f = open("data01.txt", "r")

    for line in f.readlines():
        l.append(int(line.replace("\n","")))

    f.close()

else:
    print "No list selected. Exit program"
    sys.exit(1)

def findCorrectElements(e1, e2, e3):
    print "The elements that sum up to 2020 is %i, %i and %i, and the AoC answer is %i" % (e1, e2, e3, e1*e2*e3)
    sys.exit(1)



for e1 in l: 
    for e2 in l: 
        for e3 in l:
            if (e1 + e2 + e3) == 2020:
                findCorrectElements(e1, e2, e3)
            else:
                continue


"""
# Part 1

import argparse, sys

parser = argparse.ArgumentParser("Select what list to run code for")

parser.add_argument("-l", "--list", 
                    type=int, 
                    default=2020)

args = parser.parse_args()
print type(args.list)

if args.list == 1:
    l = [1721, 979, 366, 299, 675, 1456]

elif args.list == 2:
    l = []

    f = open("data01.txt", "r")

    for line in f.readlines():
        l.append(int(line.replace("\n","")))

    f.close()

else:
    print "No list selected. Exit program"
    sys.exit(1)

def findCorrectElements(e1, e2):
    print "The elements that sum up to 2020 is %i and %i, and the AoC answer is %i" % (e1, e2, e1*e2)
    sys.exit(1)



for e1 in l: 
    for e2 in l: 
        if (e1 + e2) == 2020:
            findCorrectElements(e1, e2)
        else:
            continue


"""

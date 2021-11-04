# AoC 2020 - Day 7

# Stargazer

# ---------------------
#
# Status:
# Part 1 - Code validated and answer delivered
# Part 2 - Code validated and answer delivered
#
# ---------------------


import argparse, sys

parser = argparse.ArgumentParser("Select luggage rules")

parser.add_argument("-r", "--rules", 
                    type=str, 
                    default="2020",)


args = parser.parse_args()

if args.rules == "test":
    rules = {}

    f = open("test_data2.txt", "r")

    for lines in f.readlines():
        key, rules_list = lines.replace(".","").replace("\n", "").replace("bags","").replace("bag","").split("contain")
        key = key.strip()
        rules[key] = {}
        rule_list = rules_list.split(",")
    
        for elm in rule_list:
            num, rule = elm.strip().split(" ", 1)
            if num == "no":
                num = 0
            
            rules[key][rule] = num

    f.close()

elif args.rules == "puzzle_input":
    rules = {}

    f = open("luggage_rules.txt", "r")

    for lines in f.readlines():
        key, rules_list = lines.replace(".","").replace("\n", "").replace("bags","").replace("bag","").split("contain")
        key = key.strip()
        rules[key] = {}
        rule_list = rules_list.split(",")
    
        for elm in rule_list:
            num, rule = elm.strip().split(" ", 1)
            if num == "no":
                num = 0
            
            rules[key][rule] = num

    f.close()

else:
    print("No rule set was selected. Program terminated.")
    sys.exit(1)

#print(rules["shiny gold"]["dark red"])


start_bag = "shiny gold"

counted_bags = []

def findInnerBag(start_bag):
    global counted_bags

    innerBags = rules[start_bag]

    for bag in innerBags:

        numbOfBags = int(innerBags[bag])

        for i in range(numbOfBags):
            counted_bags.append(b for b in findInnerBag(bag))


    return counted_bags

ans = findInnerBag(start_bag)


print("The number of bags that can contain atleast one shiny gold bag is: %i" % len(ans))



"""
# Part 1

import argparse, sys

parser = argparse.ArgumentParser("Select luggage rules")

parser.add_argument("-r", "--rules", 
                    type=str, 
                    default="2020",)


args = parser.parse_args()

if args.rules == "test":
    rules = {}

    f = open("test_data.txt", "r")

    for lines in f.readlines():
        key, rules_list = lines.replace(".","").replace("\n", "").replace("bags","").replace("bag","").split("contain")
        key = key.strip()
        rules[key] = {}
        rule_list = rules_list.split(",")
    
        for elm in rule_list:
            num, rule = elm.strip().split(" ", 1)
            if num == "no":
                num = 0
            
            rules[key][rule] = num

    f.close()

elif args.rules == "puzzle_input":
    rules = {}

    f = open("luggage_rules.txt", "r")

    for lines in f.readlines():
        key, rules_list = lines.replace(".","").replace("\n", "").replace("bags","").replace("bag","").split("contain")
        key = key.strip()
        rules[key] = {}
        rule_list = rules_list.split(",")
    
        for elm in rule_list:
            num, rule = elm.strip().split(" ", 1)
            if num == "no":
                num = 0
            
            rules[key][rule] = num

    f.close()

else:
    print("No rule set was selected. Program terminated.")
    sys.exit(1)


goal = "shiny gold"

selected_bags= []

def search(outer_bag, goal):
    global selected_bags
    inner = [bag for bag in rules[outer_bag].keys() if bag != "other"]

    if inner: 
        for bag in inner:        
            if bag == goal:
                return True
            else:
                if search(bag, goal):
                    return True
    else:
        return False


def checkBag(goal):
    for outer_bag in rules:
        if search(outer_bag, goal):
            selected_bags.append(outer_bag)

    
    return len(selected_bags)

ans = checkBag(goal)


print("The number of bags that can contain atleast one shiny gold bag is: %i" % ans)

"""


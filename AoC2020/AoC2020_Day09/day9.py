# AoC 2020 - Day 9


# -------------------------
#
# Status
# Part 1 - Code validated and answer delivered
# Part 2 - Code validated and answer delivered
#
# -------------------------


import argparse, sys

parser = argparse.ArgumentParser("Select numbers")

parser.add_argument("-n", "--numbers", 
                    type=str, 
                    default="2020")

args = parser.parse_args()

if args.numbers == "test":
    num = []
    preamble = 5

    f = open("test_data.txt", "r")

    for lines in f.readlines():
        num.append(int(lines))

    f.close()
    

elif args.numbers == "puzzle_input":
    num = []
    preamble = 25

    f = open("numbers.txt", "r")

    for lines in f.readlines():
        num.append(int(lines))

    f.close()

else:
    print("No number file was selected. Program is terminated.")
    sys.exit(1)


def checkNum(num1, num2, goal):
    if num1 + num2 == goal:
        return True
    else:
        return False


def checkList(preamble, index, lst):
    global match

    for p in range(1,preamble+1):
        #print(p)
        for pp in range(1,preamble+1):
            if p != pp:

                #print(f"1: {index-p}, 2: {index-pp}")
                #print(lst[index-p], lst[index-p-1],lst[index])
                if checkNum(lst[index-p], lst[index-pp], lst[index]):
                    #print(lst[index-p])
                    #print(lst[index-pp])
                    #print(lst[index-p], lst[index-pp],lst[index])
                    match.append(lst[index])
                    #print("match")
    return None

def becomeSum(start, end, goal):
    elmSum = 0
    global elmList
    elmList = []

    for i in range(start, end+1):
        elmSum += num[i]
        elmList.append(num[i])
    if elmSum != goal:
        return False

    else:
        return True

match = []

for i in range(preamble, len(num)):
    #print(i)
    checkList(preamble, i, num)

#print(match)
noMatch = [elm for elm in num[preamble:] if elm not in match]

#print(f"The number(s) that is not a sum of previous numbers is {noMatch}")

goal = noMatch[0]

for start in range(len(num)):
    for end in range(1,len(num)):
        if start != end:
            if becomeSum(start, end, goal):
                minNum = min(elmList)
                maxNum = max(elmList)
                #weak = num[start] + num[end]
                print(f"The encryption weakness is (start:index, min val in list) {start, minNum} + (end:index, max val in list) {end, maxNum} = {minNum+maxNum} for goal {goal}")
            else:
                continue


"""
# Part 1


import argparse, sys

parser = argparse.ArgumentParser("Select numbers")

parser.add_argument("-n", "--numbers", 
                    type=str, 
                    default="2020")

args = parser.parse_args()

if args.numbers == "test":
    num = []
    preamble = 5

    f = open("test_data.txt", "r")

    for lines in f.readlines():
        num.append(int(lines))

    f.close()
    

elif args.numbers == "puzzle_input":
    num = []
    preamble = 25

    f = open("numbers.txt", "r")

    for lines in f.readlines():
        num.append(int(lines))

    f.close()

else:
    print("No number file was selected. Program is terminated.")
    sys.exit(1)


def checkNum(num1, num2, goal):
    if num1 + num2 == goal:
        return True
    else:
        return False


def checkList(preamble, index, lst):
    global match

    for p in range(1,preamble+1):
        #print(p)
        for pp in range(1,preamble+1):
            if p != pp:

                #print(f"1: {index-p}, 2: {index-pp}")
                #print(lst[index-p], lst[index-p-1],lst[index])
                if checkNum(lst[index-p], lst[index-pp], lst[index]):
                    #print(lst[index-p])
                    #print(lst[index-pp])
                    #print(lst[index-p], lst[index-pp],lst[index])
                    match.append(lst[index])
                    #print("match")
    return None


match = []

for i in range(preamble, len(num)):
    #print(i)
    checkList(preamble, i, num)

#print(match)
noMatch = [elm for elm in num[preamble:] if elm not in match]

print(f"The number(s) that is not a sum of previous numbers is {noMatch}")

"""

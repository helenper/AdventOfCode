# AoC 2020 - Day 6

# Stargazer

# -------------------------
#
# Status:
# Part 1 - Code validated and answer delivered
# Part 2 - Started
# 
# -------------------------

import argparse, sys, string

parser = argparse.ArgumentParser("Select answers per group list to count.")

parser.add_argument("-a", "--answers", 
                    type=str,
                    default="2020")

args = parser.parse_args()

if args.answers == "test":
    ans = []

    f = open("test_data.txt", "r")
    
    for lines in f.readlines():
        if lines != "\n":
            ans.append(lines.replace("\n", ""))
        else:
            ans.append(lines)

    f.close()

elif args.answers == "puzzle_input":
    ans = []

    f = open("answers.txt", "r")

    for lines in f.readlines():
        if lines != "\n":
            ans.append(lines.replace("\n", ""))
        else:
            ans.append(lines)

    f.close()

else:
    print ("No answer list is seleced. Program is terminated.")
    sys.exit(1)

def group_ans(str1):
    ansPerGroup = {}
    yesAns = 0
    keyCounts = []
    

    str_elm = str1.split(",")
    
    for i in range(len(str_elm)):
        ansPerGroup["Person"+str(i)] = {}
        for letter in str_elm[i]:
            if letter not in ansPerGroup["Person"+str(i)].keys():
                ansPerGroup["Person"+str(i)][letter] = str_elm.count(letter)
            else:
              continue
          
    for i in range(len(ansPerGroup.keys())):
            keys = ansPerGroup["Person"+str(i)].keys()
            for elm in keys:
                keyCounts.append(elm)

    counter = {i:keyCounts.count(i) for i in keyCounts}
    
    for elm in counter.keys():
        if counter[elm] >= len(str_elm):
            yesAns += 1
        else:
            continue

    return yesAns
    


answers = []
yesPerGroup = []

for i in range(len(ans)):
    try:
        j = ans.index("\n")
        answers.append((",".join(ans[0:j])))#.replace(",", ""))
        del ans[0:j+1]
    except ValueError:
        answers.append((",".join(ans[:])))#.replace(",",""))
        break

for elm in answers:
    yesPerGroup.append(group_ans(elm))

#print(answers, yesPerGroup)
print("The number of questions all in a group said yes to is %i " % sum(yesPerGroup))


"""
# Part 1

import argparse, sys, string

parser = argparse.ArgumentParser("Select answers per group list to count.")

parser.add_argument("-a", "--answers", 
                    type=str,
                    default="2020")

args = parser.parse_args()

if args.answers == "test":
    ans = []

    f = open("test_data.txt", "r")
    
    for lines in f.readlines():
        if lines != "\n":
            ans.append(lines.replace("\n", ""))
        else:
            ans.append(lines)

    f.close()

elif args.answers == "puzzle_input":
    ans = []

    f = open("answers.txt", "r")

    for lines in f.readlines():
        if lines != "\n":
            ans.append(lines.replace("\n", ""))
        else:
            ans.append(lines)

    f.close()

else:
    print ("No answer list is seleced. Program is terminated.")
    sys.exit(1)

def group_ans(str1):
    count = []

    for letter in str1:
        if letter not in count:
            count.append(letter)
        else:
            continue

    return len(count)
    


answers = []
yesPerGroup = []

for i in range(len(ans)):
    try:
        j = ans.index("\n")
        answers.append((",".join(ans[0:j])).replace(",", ""))
        del ans[0:j+1]
    except ValueError:
        answers.append((",".join(ans[:])).replace(",",""))
        break

for elm in answers:
    yesPerGroup.append(group_ans(elm))

#print(answers, yesPerGroup)
print("The total number of group 'yes' answers is: %i " % sum(yesPerGroup))

"""

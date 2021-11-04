# AoC 2020 Day 10


# -------------------------
#
# Status:
# Part 1 - 
# Part 2 - 
# 
# -------------------------


import argparse, sys

parser = argparse.ArgumentParser("Select list of adapters")

parser.add_argument("-a", "--adapter", 
                    type=str, 
                    default="2020")


args = parser.parse_args()

if args.adapter == "test":
    adapters = []

    f = open("test_data.txt", "r")

    for lines in f.readlines():
        adapters.append(int(lines))

    f.close()

elif args.adapter == "puzzle_input":

    adapters = []

    f = open("adapter.txt", "r")

    for lines in f.readlines():
        adapters.append(int(lines))

    f.close()
else:
    print("No adapter list selected. Program is terminated")
    sys.exit(1)

voltRange = [1,2,3]

deviceAdp = max(adapters) + 3
adapters.append(deviceAdp)
outlet = 0

# count events with difference in jolts
jolt1 = 0
jolt2 = 0
jolt3 = 0



def findAdapter(startV):
    #print("finding next adapter that matches", startV)
    possibleA = [a+startV for a in voltRange]

    global jolt1, jolt2, jolt3

    for a in possibleA:
        if a in sorted(adapters):
            elm = a - startV
            index = adapters.index(a)
            if elm == 1:
                jolt1 += 1
            
            elif elm == 2:
                jolt2 += 1
            
            else:
                jolt3 += 1

            del adapters[index]
            return a

            
    return startV

while outlet < deviceAdp:

    outlet = findAdapter(outlet)
    #print(outlet)
    if not adapters:
        break


print(f"Jolt 1 span {jolt1}, jolt 2 span {jolt2}, jolt 3 span {jolt3} and multiplication of number of jolts with 1 span and 3 span is (answer): {jolt1*jolt3}  ")
        





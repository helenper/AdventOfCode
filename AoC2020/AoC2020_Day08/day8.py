# AoC Day 8

# -------------------------
#
# Status:
# Part 1 - Code validated and answer delivered
# Part 2 - Code validated and answer delivered
#
# -------------------------


import argparse, sys

parser = argparse.ArgumentParser("Select boot code to run")

parser.add_argument("-bc", "--bootCode", 
                    type=str, 
                    default="2020")

args = parser.parse_args()

if args.bootCode == "test":
    
    inputCode = []

    f = open("test_data.txt", "r")

    for lines in f.readlines():
        instruction, operation = lines.replace("\n", "").split(" ")
        inputCode.append([instruction, operation])

    f.close()

elif args.bootCode == "puzzle_input": 
    inputCode = []

    f = open("boot_code.txt", "r")

    for lines in f.readlines():
        instruction, operation = lines.replace("\n", "").split(" ")
        inputCode.append([instruction, operation])

    f.close()

else:
    print("No boot code selected to run. Program terminated.")
    sys.exit(1)



def runCode(inputCode: list):
    #print("run code")
    
    global accum
    accum = 0
    i = 0
    step = []
    
    while i <= len(inputCode)-1:
        try:
            #print(i)
            if i not in step:
                step.append(i)
                #print(i)
                if i+1 != len(inputCode):
                    #print("Not reached len(inputCode)")
                    if inputCode[i][0] == "acc":
                        accum += int(inputCode[i][1])
                        i += 1

                    elif inputCode[i][0] == "jmp":
                        i += int(inputCode[i][1])

                    elif inputCode[i][0] == "nop":
                        i += 1
                    else:
                        print("Something is wrong in inputCode list. Please check input data. Program is terminated.")
                        sys.exit(1)
                else:
                    if inputCode[i][0] == "acc":
                        accum += int(inputCode[i][1])
                        i += 1

                    elif inputCode[i][0] == "jmp":
                        i += int(inputCode[i][1])

                    elif inputCode[i][0] == "nop":
                        i += 1
                    print(f"Code is finished. The accumulated score is {accum}")
                    sys.exit(1)
            else:
                break
            
        except IndexError:
             return False
     

def findIndex(elm: str):
    #print("Finding new index")
    index = []

    for i in range(len(inputCode)):
        if elm == inputCode[i][0]:
            index.append(i)
    
    return index

def changeCode(index, oldElm, newElm):
    #print(f"changing index from old {oldElm} to new {newElm} at index {index}")
    inputCode[index][0] = newElm
    #print(inputCode[index])
    if not runCode(inputCode):
        inputCode[index][0] = oldElm

        return False
    
    else:
        print(f"Program finished with accumulated value of {accum}")
        return True


def checkCode(inputCode: list):

    if not runCode(inputCode):
        #print("Not original code list correct")
        jmp_index = findIndex("jmp")
        nop_index = findIndex("nop")

        for elm in jmp_index:
            if not changeCode(elm, "jmp", "nop"):
                continue
            else:
                print("Program finished")
        
        for elm in nop_index:
            if not changeCode(elm, "nop", "jmp"):
                continue
            else:
                print("Program finished")

checkCode(inputCode)    




"""
# Part 1


import argparse, sys

parser = argparse.ArgumentParser("Select boot code to run")

parser.add_argument("-bc", "--bootCode", 
                    type=str, 
                    default="2020")

args = parser.parse_args()

if args.bootCode == "test":
    
    inputCode = []

    f = open("test_data.txt", "r")

    for lines in f.readlines():
        instruction, operation = lines.replace("\n", "").split(" ")
        inputCode.append([instruction, operation])

    f.close()

elif args.bootCode == "puzzle_input": 
    inputCode = []

    f = open("boot_code.txt", "r")

    for lines in f.readlines():
        instruction, operation = lines.replace("\n", "").split(" ")
        inputCode.append([instruction, operation])

    f.close()

else:
    print("No boot code selected to run. Program terminated.")
    sys.exit(1)


accum = 0
i = 0
step = []

while i <= len(inputCode)-1:
    if i not in step:
        step.append(i)

        if inputCode[i][0] == "acc":
            accum += int(inputCode[i][1])
            i += 1

        elif inputCode[i][0] == "jmp":
            i += int(inputCode[i][1])

        elif inputCode[i][0] == "nop":
            i += 1
        else:
            print("Something is wrong in inputCode list. Please check input data. Program is terminated.")
            sys.exit(1)
    else:
        print(f"Reached the same command at line: {i}. Program is terminated with a score for accumulator of: {accum}")
        sys.exit(1)

"""






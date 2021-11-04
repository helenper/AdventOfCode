# AoC 2019 Day 2
# Stargazer

# --------------------------------
#
# Status: Code for part 1 tested and validated - answer submitted
#
# --------------------------------


# -------------------------------
#
# Mission: Create a Intcode program
#
# -------------------------------


import argparse, sys

parser = argparse.ArgumentParser("Process list to run Intcode program on for AoC 2019 day 2")

parser.add_argument("-l", "--list", 
                    type=int,  
                    default=1202)

args = parser.parse_args()

if args.list == 1:
    l = [1, 0, 0, 0, 99]

elif args.list == 2:
    l = [2, 3, 0, 3, 99]

elif args.list == 3:
    l = [2, 4, 4, 5, 99, 0]

elif args.list == 4: 
    l = [1, 1, 1, 4, 99, 5, 6, 0, 99]

elif args.list == 5: 
    l = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,6,23,2,13,23,27,1,27,13,31,1,9,31,35,1,35,9,39,1,39,5,43,2,6,43,47,1,47,6,51,2,51,9,55,2,55,13,59,1,59,6,63,1,10,63,67,2,67,9,71,2,6,71,75,1,75,5,79,2,79,10,83,1,5,83,87,2,9,87,91,1,5,91,95,2,13,95,99,1,99,10,103,1,103,2,107,1,107,6,0,99,2,14,0,0]

else: 
    l = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,6,23,2,13,23,27,1,27,13,31,1,9,31,35,1,35,9,39,1,39,5,43,2,6,43,47,1,47,6,51,2,51,9,55,2,55,13,59,1,59,6,63,1,10,63,67,2,67,9,71,2,6,71,75,1,75,5,79,2,79,10,83,1,5,83,87,2,9,87,91,1,5,91,95,2,13,95,99,1,99,10,103,1,103,2,107,1,107,6,0,99,2,14,0,0]


# ----------------
#
# Functions
#
# ----------------

def finished (n, v):

    print "---------------------"
    print ""
    print "n: %i    v: %i " % (n,v)
    print "AoC answer: %i" % (100*n + v)
    print ""
    print "---------------------"

    sys.exit(1)


# ----------------
#
# Definitions and program body
#
# ----------------

opt1 = 1    # addition
opt2 = 2    # multiplication
opt99 = 99  # stop

idx0 = 0
idx1 = 0
idx2 = 0
idx3 = 0

noun = [x for x in range(0,100)]
verb = noun

for n in noun:
    for v in verb:
        
        # Check if l_copy exists, delete it if yes, create if no
        try:
            del l_copy
        except: 
            l_copy = []

        # Make (REAL!) copy of list l and insert n and v test values
        l_copy = l[:]
        l_copy[1] = n
        l_copy[2] = v
        
        i = 0
        
        while i <= (len(l_copy)-1):
            if l_copy[0] == 19690720:

                finished(n, v)
                """
                print "---------------------"
                print ""
                print "n: %i    v: %i i: %i" % (n,v, i)
                print ""
                print "---------------------"

                print l_copy[0]
                break
                """

            else:    
                if l_copy[i] == opt99:
                    print "Program finished, reached integer value of 99 as instruction at index value i = %i while lengt of list was %i for test values n = %i and v = %i." % (i, len(l_copy), n, v)
                    i += 4
                    break

                if l_copy[i] == opt1:
                    # Addition
                    try:
                        #print "addition: ", i, len(l_copy), i+1
                        idx1 = l_copy[i+1]
                        idx2 = l_copy[i+2]
                        idx3 = l_copy[i+3]

                        l_copy[idx3] = l_copy[idx1] + l_copy[idx2]

                        i += 4
                    except IndexError:
                        print "Next step goes out of list index range. Break"
                        break

                else:
                    #Multiplication
                    try:
                        #print "multiplication: ", i, len(l_copy), i+1
                        idx1 = l_copy[i+1]
                        idx2 = l_copy[i+2]
                        idx3 = l_copy[i+3]

                        l_copy[idx3] = l_copy[idx1] * l_copy[idx2]

                        i += 4

                    except IndexError:
                        print "Next step goes out of list index range. Break"
                        break


"""
# Part 1

import argparse

parser = argparse.ArgumentParser("Process list to run Intcode program on for AoC 2019 day 2")

parser.add_argument("-l", "--list", 
                    type=int,  
                    default=1201)

args = parser.parse_args()

if args.list == 1:
    l = [1, 0, 0, 0, 99]

elif args.list == 2:
    l = [2, 3, 0, 3, 99]

elif args.list == 3:
    l = [2, 4, 4, 5, 99, 0]

elif args.list == 4: 
    l = [1, 1, 1, 4, 99, 5, 6, 0, 99]


elif args.list == 5: 
    l = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,6,23,2,13,23,27,1,27,13,31,1,9,31,35,1,35,9,39,1,39,5,43,2,6,43,47,1,47,6,51,2,51,9,55,2,55,13,59,1,59,6,63,1,10,63,67,2,67,9,71,2,6,71,75,1,75,5,79,2,79,10,83,1,5,83,87,2,9,87,91,1,5,91,95,2,13,95,99,1,99,10,103,1,103,2,107,1,107,6,0,99,2,14,0,0]

else: 
    l = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,6,23,2,13,23,27,1,27,13,31,1,9,31,35,1,35,9,39,1,39,5,43,2,6,43,47,1,47,6,51,2,51,9,55,2,55,13,59,1,59,6,63,1,10,63,67,2,67,9,71,2,6,71,75,1,75,5,79,2,79,10,83,1,5,83,87,2,9,87,91,1,5,91,95,2,13,95,99,1,99,10,103,1,103,2,107,1,107,6,0,99,2,14,0,0]

opt1 = 1    # addition
opt2 = 2    # multiplication
opt99 = 99  # stop

idx0 = 0
idx1 = 0
idx2 = 0
idx3 = 0

i = 0

while i < len(l)-1:
    if l[i] == opt99:
        print "Program finished, reached integer value of 99 at index 0."
        break
    elif l[i] == opt1:
        # Addition
        #while i < len(l)-1:
            try:
                print "addition: ", i, len(l), i+1
                idx1 = l[i+1]
                idx2 = l[i+2]
                idx3 = l[i+3]

                l[idx3] = l[idx1] + l[idx2]

                i += 4
            except IndexError:
                print "Next step goes out of list index range. Break"
                break

    else:
        #Multiplication
            try:
                print "multiplication: ", i, len(l), i+1
                idx1 = l[i+1]
                idx2 = l[i+2]
                idx3 = l[i+3]

                l[idx3] = l[idx1] * l[idx2]

                i += 4

            except IndexError:
                print "Next step goes out of list index range. Break"
                break
print l

"""


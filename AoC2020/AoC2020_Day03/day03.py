# AoC 2020 - Day 3

# Stargazer


# -------------------
#
# Stauts:
# Part 1: code validated and answer delivered
# Part 2: started
#
# -------------------

import argparse, sys
import numpy as np


parser = argparse.ArgumentParser("Select map of trees")

parser.add_argument("-t", "--treeMap", 
                    type=str,
                    default=2020)


args = parser.parse_args()

if args.treeMap == "test":
    trees = ["..##.......",
             "#...#...#..",
             ".#....#..#.",
             "..#.#...#.#",
             ".#...##..#.",
             "..#.##.....",
             ".#.#.#....#",
             ".#........#",
             "#.##...#...",
             "#...##....#",
             ".#..#...#.#"]

    for i in range(len(trees)):
        trees[i] = trees[i]*10

elif args.treeMap == "puzzle_input":
    trees = []

    f = open("treepattern.txt", "r")
    for lines in f.readlines():
        trees.append(lines.replace("\n", "")*100)

    f.close()

else: 
    print ("No selected map of trees. Program terminating")
    sys.exit(1)

#move1 = [1, 3, 5, 7, 1] # to the right for different paths
#move2 = [1, 1, 1, 1, 2] # down for different paths
moves = [(1,1), (3,1), (5,1), (7,1), (1,2)] # moves for different paths (right,down)

numberOfTrees = []


for move in moves:
    m1 = move[0]
    m2 = move[1]

    xpos = 0
    ypos = 0
    numberOfTreesCurrent = 0

    print ("----------")
    print ("Now running m1 = %i and m2 = %i" % (m1, m2))
    

    for i in range(len(trees)):
        xpos = i*m1
        ypos = i*m2
    
        if xpos > len(trees[0]) or ypos > len(trees):
            print ("***********************")
            print("Has reached the end of eiter x or y position of list for m1 = %i and m2 = %i" % (m1, m2))
            print("xpos = %i while lenght of list string = %i and ypos = %i while lenght of list = %i" % (xpos, len(trees[0]), ypos, len(trees)))
            print ("")
            break

        else:
            if trees[ypos][xpos] == "#":
                print("Hit a tree")
                numberOfTreesCurrent += 1

    numberOfTrees.append(numberOfTreesCurrent)
    
AoCanswer = np.prod(numberOfTrees)


print("-----------------")
print("")
print("The answer is %i " % AoCanswer)
print("")
print("-----------------")



"""
# Part 1


import argparse, sys


parser = argparse.ArgumentParser("Select map of trees")

parser.add_argument("-t", "--treeMap", 
                    type=str,
                    default=2020)


args = parser.parse_args()

if args.treeMap == "test":
    trees = ["..##.......",
             "#...#...#..",
             ".#....#..#.",
             "..#.#...#.#",
             ".#...##..#.",
             "..#.##.....",
             ".#.#.#....#",
             ".#........#",
             "#.##...#...",
             "#...##....#",
             ".#..#...#.#"]

    for i in range(len(trees)):
        trees[i] = trees[i]*10

elif args.treeMap == "puzzle_input":
    trees = []

    f = open("treepattern.txt", "r")
    for lines in f.readlines():
        trees.append(lines.replace("\n", "")*100)

    f.close()

else: 
    print ("No selected map of trees. Program terminating")
    sys.exit(1)

move1 = 3 #to the right
move2 = 1 #down

xpos = 0
ypos = 0
numberOfTrees = 0

for i in range(len(trees)):
    xpos = i*move1
    ypos = i*move2
    
    if xpos > len(trees[0]) or ypos > len(trees):
        print("Has reached the end of eiter x or y position of list")
        print("xpos = %i while lenght of list string = %i and ypos = %i while lenght of list = %i" % (xpos, len(trees[0]), ypos, len(trees)))
        break

    else:
        if trees[ypos][xpos] == "#":
            print("Hit a tree")
            numberOfTrees += 1
    
print("-----------------")
print("")
print("The number of trees hit and answer is %i" % numberOfTrees)
print("")
print("-----------------")


"""

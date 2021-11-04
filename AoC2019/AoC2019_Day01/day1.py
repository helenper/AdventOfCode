# AoC 2019 - Day 1
# Stargazer

# -----------------------------------------
#
# Status: Code part 1 + part 2 correct and answer delivered
#
# -----------------------------------------


# Part 2

import math

file1 = open("day1_data.txt", "r")

s = 0
try:
    for lines in file1.readlines():
        l = int(lines)
        fuelForModule = math.floor((l/3.0)) - 2
        s += fuelForModule

        fuelForFuel = fuelForModule

        while fuelForFuel > 0: 
            fuelFF = math.floor((fuelForFuel/3.0)) - 2 
            if fuelFF > 0: 
                s += fuelFF
                fuelForFuel = fuelFF
            else:
                break
    
    file1.close()

except:
    # Test run with values from task
    modules = [12, 14, 1969, 100756]
    for module in modules:
        fuelForModule = math.floor((module/3.0)) - 2 
        s += fuelForModule

        fuelForFuel = fuelForModule

        while fuelForFuel > 0: 
            fuelFF = math.floor((fuelForFuel/3.0)) - 2 
            if fuelFF > 0: 
                s += fuelFF
                fuelForFuel = fuelFF
            else:
                break


print "Fuel needed: ", int(s)



"""
# Part 1

import math

file1 = open("day1_data.txt", "r")

s = 0
try:
    for lines in file1.readlines():
        l = int(lines)
        fuleForModule = math.floor((l/3.0)) - 2
        s += fuleForModule

    file1.close()
except:
    # Test run with values from task
    modules = [12, 14, 1969, 100756]
    for module in modules:
        fuleForModule = math.floor((module/3.0)) - 2
        s += fuleForModule

print int(s)
"""

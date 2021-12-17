# Day 1 - AoC2021

import numpy as np


def set_initial():
    prev = ''
    new = ''
    count = 0
    return None


# Part 1
def part1():
    prev = ''
    new = ''
    count = 0
    measurements = open('../txt_input/day01.txt', 'r')
    for lines in measurements.readlines():
        new = eval(lines)

        if prev != '': 
            if new > prev:
                count += 1
                
        prev = new

    print("The number of times the depth increase in part 1 is: %s" % count)
    return None


#Part 2
def part2():
    prev = ''
    new = ''
    count = 0
    sum_old = 0

    measurements = open('../txt_input/day01.txt', 'r')
    lines = measurements.readlines()
    max_line = len(lines)
    num_of_sections = int(np.floor(max_line/3))
    
    for i in range(1,max_line):
        sum = 0
        try:
            sum = int(lines[i-1]) + int(lines[i]) + int(lines[i+1])
            print(sum)
            if sum_old != 0:
                if sum_old < sum:
                    count += 1
            sum_old = sum
        except IndexError:
            print("The number of times the depth increase in part 2 is: %s" % count)

    return None 
        

part1()
part2()

# Advent of code - Day 6

import argparse, sys
import numpy as np

parser = argparse.ArgumentParser("Process list to run program for AoC 2021 day 5")

parser.add_argument('-t', '--test', 
                    type=str, 
                    choices=('true','false'),
                    default='true', 
                    )

parser.add_argument('-d', '--days', 
                    type=int, 
                    default=18, 
                    )

args = parser.parse_args()


if args.test == 'true':
    print('------------------')
    print('Run on test data')
    print('------------------')
else:
    print('------------------')
    print('Run on puzzle data')
    print('------------------')


def setup():
    if args.test == 'true':
        fishes = [ int(f) for f in next(open('../txt_input/day_06_test.txt')).strip().split(',') ]
  
    else:
        fishes = [ int(f) for f in next(open('../txt_input/day_06.txt')).strip().split(',') ]
    
    days = args.days
    fish_dict = {}
    key_list = [i for  i in range(9)]
    
    for key in key_list: 
        fish_dict[key] = fishes.count(key)

    return fish_dict, days


def reproduce_fish(current):

    new_state = {}
    fish_reproduce = current[0]

    new_state[0] = current[1]    
    new_state[1] = current[2]
    new_state[2] = current[3]
    new_state[3] = current[4]
    new_state[4] = current[5]
    new_state[5] = current[6]
    new_state[6] = current[7] + fish_reproduce
    new_state[7] = current[8]
    new_state[8] = fish_reproduce

    return new_state




def part1and2():
    fishes, days = setup()
    #print('Initial', fishes, type(fishes))

    for i in range(days):
        fishes = reproduce_fish(fishes)
        #print(fishes_count)
        
    
    sum_fish = 0
    for key in fishes.keys():
        sum_fish += fishes[key] 


    print(f"The answer to part 1 is that after {days} days there are {sum_fish} fish.")

part1and2()
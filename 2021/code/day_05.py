# Advent of code - Day 5

import argparse, sys
import numpy as np

parser = argparse.ArgumentParser("Process list to run program for AoC 2021 day 5")

parser.add_argument('-t', '--test', 
                    type=str, 
                    choices=('true','false'),
                    default='true', 
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
        infile = open('../txt_input/day_05_test.txt', 'r')
  
    else:
        infile = open('../txt_input/day_05.txt', 'r')


    return infile


def coordinates(infile):

    start_cord = []
    end_cord = []
    cord_ulist = []

    for lines in infile.readlines():
        start = lines.split(' ')[0].strip()
        end = lines.split(' ')[-1].strip()

        start_x, start_y = start.split(',')
        end_x, end_y = end.split(',')
        
        start_cord.append([start_x, start_y])
        end_cord.append([end_x, end_y])
        cord_ulist.append(start_x)
        cord_ulist.append(start_y)
        cord_ulist.append(end_x)
        cord_ulist.append(end_y)
    
    max_point = max(cord_ulist)

    infile.close()
    return start_cord, end_cord, max_point


def mark_coordinates(start_point, end_point, vents, diagonal=False):
    x1 = int(start_point[0])
    y1 = int(start_point[1])
    x2 = int(end_point[0])
    y2 = int(end_point[1])

    y_start = min(y1, y2)
    y_end = max(y1, y2)
    x_start = min(x1, x2)
    x_end = max(x1, x2)
    
    if x1 == x2 or y1 == y2:
        if y1 == y2: 
            i = y1
            for j in range(x_start, x_end+1):
                vents[i][j] += 1      
        elif x1 == x2: 
            j = x1
            for i in range(y_start, y_end+1):
                vents[i][j] += 1
    else:
            if diagonal == True:

                if x1 > x2:
                    x = [x_ for x_ in range(x2, x1 + 1)]
                    x.reverse()
                else: 
                    x = [x_ for x_ in range(x1, x2+1)]
                
                if y1 > y2: 
                    y = [y_ for y_ in range(y2, y1 + 1)]
                    y.reverse()
                else: 
                    y = [y_ for y_ in range(y1, y2+1)]
                
                for i,j in zip(x,y):
                    vents[j][i] += 1
               
    return None


def part1():
    infile = setup()
    start_cord, end_cord, max_point = coordinates(infile)
    vents =  np.zeros(( int(max_point)+1, int(max_point)+1))

    for x, y in zip(start_cord, end_cord):
        mark_coordinates(x, y, vents)

    unique, count = np.unique(vents, return_counts=True)
    count_dic= dict(zip(unique, count))

    sum_gt2 = 0

    for key in count_dic.keys():
        if key >= 2: 
            sum_gt2 += count_dic[key]
    
    print(f'The answer to part 1 is {sum_gt2}')


def part2():
    infile = setup()
    start_cord, end_cord, max_point = coordinates(infile)
    vents =  np.zeros(( int(max_point)+1, int(max_point)+1))

    for x, y in zip(start_cord, end_cord):
        mark_coordinates(x, y, vents, True)

    unique, count = np.unique(vents, return_counts=True)
    count_dic= dict(zip(unique, count))

    sum_gt2 = 0

    for key in count_dic.keys():
        if key >= 2: 
            sum_gt2 += count_dic[key]
    
    print(f'The answer to part 2 is {sum_gt2}')


part1()
part2()
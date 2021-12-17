# Day 4 - Advent of Code 2021

import numpy as np
from itertools import islice

def create_board(l):
    i = 0
    boards = {}
    while i*5 < len(l):
        board = l[0 + i*5 :5 +5*i]
        boards[i] = board
        i += 1
    
    return boards

def mark_numb(boards, numb, keys_w_bingo):
    horisontal = 0

    for key in boards.keys():
        if key not in keys_w_bingo:
            for i in range(len(boards[key])):
                if numb in boards[key][i]:
                    idx = boards[key][i].index(numb)
                    boards[key][i][idx] = 'X'
                horisontal = boards[key][i].count('X')
                if horisontal == 5:
                    keys_w_bingo.append(key)
                    return key, 'bingo'
                v_count = count_vertical(boards[key])
                if v_count == 5: 
                    keys_w_bingo.append(key)
                    return key, 'bingo'
    
    return None, 'not bingo'


def count_vertical(board):
    for i in range(len(board)):
        vertical = []
        for j in range(len(board)):
            vertical.append(board[j][i])
        v_count = vertical.count('X')
        if v_count == 5: 
            return v_count
            break
    return 0



def part1():
    winner_board = []
    winner_drawn_numb = []
    winner_sum = 0
    keys_with_bingo = []
    
    # Test
    #infile = open('../txt_input/day_04_test.txt', 'r')

    infile = open('../txt_input/day_04.txt', 'r')

    drawn_numb = infile.readline().strip().split(',')
    gather_list = []    

    for lines in infile.readlines():
        if lines != '\n':
            line = lines.strip().split(' ')
            while ('' in line):
                line.remove('')
            gather_list.append(line)
    
            #print(line)

    boards = create_board(gather_list)
    
    for numb in drawn_numb:
            key, string = mark_numb(boards, numb, keys_with_bingo)
            if string == 'bingo':
                winner_board.append(key)
                winner_drawn_numb.append(numb)
                break

    for elm in boards[winner_board[0]]:
        for e in elm:
            if e != 'X':
                winner_sum += int(e)
    score = int(winner_drawn_numb[0]) * int(winner_sum)
    print('Answer to part 1: Winner is board %s with a score of %s' % (winner_board[0], score))
    infile.close()


def part2():
    winner_board = []
    winner_drawn_numb = []
    winner_sum = 0
    keys_with_bingo = []
    
    # Test
    #infile = open('../txt_input/day_04_test.txt', 'r')

    infile = open('../txt_input/day_04.txt', 'r')

    drawn_numb = infile.readline().strip().split(',')
    gather_list = []    

    for lines in infile.readlines():
        if lines != '\n':
            line = lines.strip().split(' ')
            while ('' in line):
                line.remove('')
            gather_list.append(line)
    
            #print(line)

    boards = create_board(gather_list)
    #print(boards.keys())
    
    for numb in drawn_numb:
        for i in range(len(boards.keys())):
            key, string = mark_numb(boards, numb, keys_with_bingo)
            if string == 'bingo':
                winner_board.append(key)
                winner_drawn_numb.append(numb)

    for elm in boards[winner_board[-1]]:
        for e in elm:
            if e != 'X':
                winner_sum += int(e)
    score = int(winner_drawn_numb[-1]) * int(winner_sum)
    print('Answer to part 2: The last board to win is board %s with a score of %s' % (winner_board[-1], score))
    infile.close()

part1()
part2()
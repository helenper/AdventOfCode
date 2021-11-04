# AoC 2020 - Day 5

# Stargazer

# -------------------------
#
# Status:
# Part 1 - Code validated and answer delivered
# Part 2 - Code validated and answer delivered
# 
# -------------------------


import argparse, sys

parser = argparse.ArgumentParser("Select which boarding pass inputs to scan")

parser.add_argument("-bp", "--boarding_pass", 
                    type=str,
                    default="2020")

args = parser.parse_args()

if args.boarding_pass == "test":
    boarding_passes = []
    f = open("test_data.txt", "r")

    for lines in f.readlines():
        boarding_passes.append(lines.replace("\n", ""))

    f.close()

elif args.boarding_pass == "puzzle_input":
    boarding_passes = []
    f = open("boarding_passes.txt", "r")

    for lines in f.readlines():
        boarding_passes.append(lines.replace("\n", ""))
    
    f.close()

else:
    print ("No input borarding passes was selected. Program is terminated.")
    sys.exit(1)


class Boardingpass:
    def __init__(self, boardingpass, row = None, column = None, seatID = None):
        self.boardingpass = boardingpass
        self.row = row
        self.column = column
        self.seatID = seatID

        self.find_seat(self.boardingpass)

    def half_list(self, list_input, letter):
        half = len(list_input)//2
        if letter == "F" or letter == "L":
            return list_input[:half]
        elif letter == "B" or letter == "R":
            return list_input[half:]
    
    def find_seat(self, boardingpass):
        self.row = self.find_row(self.boardingpass[:7])
        self.column = self.find_column(self.boardingpass[-3:])
        self.seatID = self.row * 8 + self.column

    def find_row(self, boardingpass):
        row_first = 0
        row_last = 127
        rows = [x for x in range(row_first,row_last+1)]

        for elm in boardingpass:
            rows = self.half_list(rows, elm)
        return rows[0]

    def find_column(self, boardingpass):
        column_first = 0
        column_last = 7

        columns = [x for x in range(column_first, column_last +1)]
        
        for elm in boardingpass:
            columns = self.half_list(columns, elm)
        return columns[0]


boarding_pass = [0]*len(boarding_passes)
seatIDs = [0]*len(boarding_pass)

for i in range(len(boarding_passes)):
    boarding_pass[i] = Boardingpass(boarding_passes[i])
    seatIDs[i] = boarding_pass[i].seatID


def missing_numb(lst):
    return [x for x in range(sorted(seatIDs)[0], sorted(seatIDs)[-1]+1) if x not in sorted(seatIDs)]

print ("Our seatID is: %i" % missing_numb(seatIDs)[0])



"""
# Part 1


import argparse, sys

parser = argparse.ArgumentParser("Select which boarding pass inputs to scan")

parser.add_argument("-bp", "--boarding_pass", 
                    type=str,
                    default="2020")

args = parser.parse_args()

if args.boarding_pass == "test":
    boarding_passes = []
    f = open("test_data.txt", "r")

    for lines in f.readlines():
        boarding_passes.append(lines.replace("\n", ""))

    f.close()

elif args.boarding_pass == "puzzle_input":
    boarding_passes = []
    f = open("boarding_passes.txt", "r")

    for lines in f.readlines():
        boarding_passes.append(lines.replace("\n", ""))
    
    f.close()

else:
    print ("No input borarding passes was selected. Program is terminated.")
    sys.exit(1)


class Boardingpass:
    def __init__(self, boardingpass, row = None, column = None, seatID = None):
        self.boardingpass = boardingpass
        self.row = row
        self.column = column
        self.seatID = seatID

        self.find_seat(self.boardingpass)

    def half_list(self, list_input, letter):
        half = len(list_input)//2
        if letter == "F" or letter == "L":
            return list_input[:half]
        elif letter == "B" or letter == "R":
            return list_input[half:]
    
    def find_seat(self, boardingpass):
        self.row = self.find_row(self.boardingpass[:7])
        self.column = self.find_column(self.boardingpass[-3:])
        self.seatID = self.row * 8 + self.column

    def find_row(self, boardingpass):
        row_first = 0
        row_last = 127
        rows = [x for x in range(row_first,row_last+1)]

        for elm in boardingpass:
            rows = self.half_list(rows, elm)
        return rows[0]

    def find_column(self, boardingpass):
        column_first = 0
        column_last = 7

        columns = [x for x in range(column_first, column_last +1)]
        
        for elm in boardingpass:
            columns = self.half_list(columns, elm)
        return columns[0]


boarding_pass = [0]*len(boarding_passes)
seatIDs = [0]*len(boarding_pass)

for i in range(len(boarding_passes)):
    boarding_pass[i] = Boardingpass(boarding_passes[i])
    seatIDs[i] = boarding_pass[i].seatID

print ("The highest seatID value is: %i" % max(seatIDs))

"""

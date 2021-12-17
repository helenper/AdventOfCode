# Day 3 - AoC2021

#Part 1


def part1():
    gamma = []
    epsilon = []

    lines = open('../txt_input/day_03.txt', 'r').readlines()

    for i in range(len(lines[0])-1):
        bit = []
        for j in range(len(lines)):
            bit.append(lines[j][i])

        zeros = bit.count('0')
        ones = bit.count('1')

        if zeros > ones:
            gamma.append('0')
            epsilon.append('1')
        else:
            gamma.append('1')
            epsilon.append('0')

        bit.clear()

    gamma10 = int(''.join(x for x in gamma), 2)
    epsilon10 = int(''.join(x for x in epsilon), 2)
    
    print("The result from part 1 is %s." % (gamma10*epsilon10))



# Part 2

def check_value(value, index, lists):
    if len(lists) > 1:
        for elm in lists[:]:
            if elm[index] != value:
                lists.remove(elm)
    return None

def count_and_check_values(lists, goal_type):
    index_range = len(lists[0])
    for i in range(index_range):
        for elm in lists:
            bit = []
            for j in range(len(lists)):
                bit.append(lists[j][i])

            zeros = bit.count('0')
            ones = bit.count('1')

        if goal_type == 'oxy':
            if zeros > ones:
                check_value('0', i, lists)
            elif zeros < ones:
                check_value('1', i, lists)
            else: 
                check_value('1', i, lists)

        if goal_type == 'co2':  
            if zeros > ones:
                check_value('1', i, lists)
            elif zeros < ones:
                check_value('0', i, lists)
            else: 
                check_value('0', i, lists)


def part2():
    #test case
    #lines = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
    
    f= open('../txt_input/day_03.txt', 'r')
    lines = []

    for l in f.readlines():
       lines.append(l.replace('\n', ''))
    
    oxy = lines[:]
    co2 = lines[:]

    count_and_check_values(oxy, 'oxy')
    count_and_check_values(co2, 'co2')
   
    #print(oxy, co2)
    
    oxygen_gen = int(oxy[0], 2)
    co2_rating = int(co2[0], 2)
    
    print("The result from part 2 is %s." % (oxygen_gen*co2_rating))

part1()
part2()
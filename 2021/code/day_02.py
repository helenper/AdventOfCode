#Day 2 - AoC2021

#Part 1
def part1():
    horisontal = 0
    vertical = 0

    for lines in open('../txt_input/day_02.txt','r').readlines():
        l = lines.split(' ')
        if l[0] == 'forward':
            horisontal += int(l[1])
        elif l[0] == 'up':
            vertical -= int(l[1])
        else:
            # l[0] == 'down'
            vertical += int(l[1])

    print("The result of part 1 is %s." % (horisontal*vertical))


#Part 2
def part2():
    horisontal = 0
    vertical = 0
    aim = 0

    for lines in open('../txt_input/day_02.txt','r').readlines():
        l = lines.split(' ')
        if l[0] == 'forward':
            horisontal += int(l[1])
            vertical += aim * int(l[1])
        elif l[0] == 'up':
            aim -= int(l[1])
        else:
            # l[0] == 'down'
            aim += int(l[1])

    print("The result of part 2 is %s." % (horisontal*vertical))


part1()
part2()
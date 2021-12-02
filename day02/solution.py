from functools import reduce

def process_line(location, change):
    return {
        'forward': lambda position, val: [position[0] + val, position[1]],
        'down': lambda position, val: [position[0], position[1] + val],
        'up': lambda position, val: [position[0], position[1] - val]
    }[change[0]](location, change[1])

def solve1(input_list):
    return reduce(lambda x, y: process_line(x, y), input_list, [0, 0])

def process_line2(location, change):
    return {
        'forward': lambda position, val: [position[0] + val, position[1] +(val*position[2]), position[2]],
        'down': lambda position, val: [position[0], position[1], position[2] + val],
        'up': lambda position, val: [position[0], position[1], position[2] - val]
    }[change[0]](location, change[1])

def solve2(input_list):
    return reduce(lambda x, y: process_line2(x, y), input_list, [0, 0, 0])

def printAnswer(position):
    print(position[0]*position[1])

input_list = [(d, int(val)) for d, val in [line.split() for line in open('input.txt')]]
printAnswer(solve1(input_list))
printAnswer(solve2(input_list))

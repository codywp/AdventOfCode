import numpy as np
from functools import reduce

def solve1(input_array):
    counts = np.sum(input_array, axis=0)
    gamma = ''.join(['1' if count >= len(input_array)/2 else '0' for count in counts])
    epsilon = ''.join(['0' if count >= len(input_array)/2 else '1' for count in counts])
    print(int(gamma, 2) * int(epsilon, 2))

def filter_list(array, col, trueVal, falseVal):
    column = array[:, col]
    bit = trueVal if sum(column) >= len(column)/2 else falseVal
    return list(filter(lambda row: row[col] == bit, array))

def solve2(input_array):
    o2gen = reduce(
        lambda array, col: array if len(array) == 1 else filter_list(np.array(array), col, 1, 0),
        range(0, 12),
        input_array
    )[0]
    co2scrub = reduce(
        lambda array, col: array if len(array) == 1 else filter_list(np.array(array), col, 0, 1),
        range(0, 12),
        input_array
    )[0]
    print(int(''.join([str(i) for i in o2gen]), 2) * int(''.join([str(i) for i in co2scrub]), 2))

input_array = [[int(c) for c in line] for line in [line.strip() for line in open('input.txt')]]
solve1(input_array)
solve2(input_array)

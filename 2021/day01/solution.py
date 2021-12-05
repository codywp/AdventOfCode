def solve1(input_list):
    return sum([input_list[i] > input_list[i-1] for i in range(1, len(input_list))])

def solve2(input_list):
    return solve1([x+y+z for x,y,z in zip(input_list[:-2], input_list[1:-1], input_list[2:])])

input_list = [int(line) for line in open('input.txt')]
print(solve1(input_list), solve2(input_list))

import re
from collections import Counter

class Line:
    def __init__(self, line):
        self.A = (int(line[0]), int(line[1]))
        self.B = (int(line[2]), int(line[3]))

    def difference(self):
        return int(self.B[0] - self.A[0]), int(self.B[1] - self.A[1])

    def skip_check(self, part2):
        dx, dy = self.difference()
        return not part2 and dx and dy

    def get_range(self, diff):
        slope = int(diff/abs(diff))
        return range(0, diff+slope, slope)

    def map_line(self):
        dx, dy = self.difference()
        if not dx: return [(self.A[0], self.A[1]+i) for i in self.get_range(dy)]
        if not dy: return [(self.A[0]+i, self.A[1]) for i in self.get_range(dx)]
        return [(self.A[0]+i, self.A[1]+j) for i,j in zip(self.get_range(dx), self.get_range(dy))]

def solve(input_list, part2=0):
    intersections = Counter()
    for line in input_list:
        if line.skip_check(part2): continue
        for point in line.map_line():
            intersections[point] = intersections[point] + 1 if point in intersections else 0
    print(len(+intersections))


input_list = [Line(re.findall('(\d+),(\d+) -> (\d+),(\d+)', line.strip())[0]) for line in open('input.txt')]
solve(input_list)
solve(input_list, True)

#first prob
with open('input.txt') as f:
    lines = f.readlines()

tot = 0
for i in range(len(lines)):
    j = 0
    while j < len(lines[i]):
        while j <= len(lines[i]) - 1 and lines[i][j] not in "1234567890":
            j += 1
        if j >= len(lines[i]):
            break
        fp = j
        while j <= len(lines[i]) - 1 and lines[i][j] in "1234567809":
            j += 1
        if j >= len(lines[i]):
            break
        lp = j - 1
        curnum = int(lines[i][fp:lp+1])
        start = 0 if fp == 0 else fp - 1
        end = lp if lp == len(lines[i]) - 2 else lp + 1
        if i == 0:
            if (lines[i][start] in ".1234567890") and (lines[i][end] in ".1234567890") and (lines[i+1][start:end+1] == ("." * (end-start+1))):
                tot -= curnum
        elif i == len(lines) - 1:
            if (lines[i][start] in ".1234567890") and (lines[i][end] in ".1234567890") and (lines[i-1][start:end+1] == ("." * (end-start+1))):
                tot -= curnum
        else:
            if (lines[i][start] in ".1234567890") and (lines[i][end] in ".1234567890") and (lines[i+1][start:end+1] == ("." * (end-start+1))) and (lines[i-1][start:end+1] == ("." * (end-start+1))):
                tot -= curnum
        tot += curnum
        j += 1

print(tot)

#second prob(copied)
import re, math
def part2(data):
    nums, symbols = parse_input(data)
    _sums = 0

    for pos, symbol in symbols.items():
        if symbol == "*":
            r, c = pos
            adj_pos = [(r + x, c + y) for x in [-1, 0, 1] for y in [-1, 0, 1]]
            adj_nums = set([nums[pos] for pos in adj_pos if pos in nums])
            if len(adj_nums) == 2:
                _sums += math.prod([item[0] for item in adj_nums])

    return _sums

def parse_input(data):
    nums = {}
    syms = {}
    idx_num = 0

    for r, line in enumerate(data):
        line_nums = re.sub(r"\D", " ", line).split()
        offset = 0
        for n in line_nums:
            pos = line.index(n, offset)
            for step in range(len(n)):
                nums[(r, pos + step)] = (int(n), idx_num)
            offset = pos + len(n)
            idx_num += 1

        line_syms = re.sub(r"[\d\.]", " ", line).split()
        offset = 0
        for sym in line_syms:
            pos = line.index(sym, offset)
            syms[(r, pos)] = sym
            offset = pos + 1

    return nums, syms

with open("input.txt") as f:
    data = f.readlines()

print(part2(data))


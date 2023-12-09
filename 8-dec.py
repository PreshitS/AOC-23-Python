with open("input.txt") as f:
    lines = f.readlines()

seq = lines[0]
hm = {}

for i in range(2, len(lines)):
    hm[lines[i][:3]] = [lines[i][7:10], lines[i][12:15]]

count = 0
cur = 'AAA'

i = 0
while cur != 'ZZZ' and i < len(seq):
    if seq[i] == 'L':
        cur = hm[cur][0]
    else:
        cur = hm[cur][1]
    count += 1
    i += 1
    if i == len(seq)-1:
        i = 0

print(count)

#second_prob
with open("input.txt") as f:
    lines = f.readlines()

seq = lines[0]
hm = {}

for i in range(2, len(lines)):
    hm[lines[i][:3]] = [lines[i][7:10], lines[i][12:15]]

arr = []
for i in hm:
    if i[-1] == 'A':
        arr.append(i)

counts = []


def cal(cur, counts):        
    count = 0
    i = 0
    while cur[-1] != 'Z' and i < len(seq):
        if seq[i] == 'L':
            cur = hm[cur][0]
        else:
            cur = hm[cur][1]
        count += 1
        i += 1
        if i == len(seq)-1:
            i = 0

    counts.append(count)

for i in arr:
    cal(i, counts)

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

num = counts[0]
for i in range(1, len(counts)):
    num = lcm(num, counts[i])

print(num)
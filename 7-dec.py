with open("input.txt") as f:
    lines = f.readlines()

hm = {}
for i in range(len(lines)):
    hm[lines[i][:5]] = [int(lines[i][6:])]

for i in hm:
    rank = 0
    for j in i:
        rank = max(rank, i.count(j))
    hm[i].append(rank)

arr = [[], [], [], [], []]
for i in hm:
    arr[hm[i][1] - 1].append(i)

for i in arr:
    if len(i) > 0:
        i.sort(reverse = True)

tot = 0
dummy = []
for i in arr:
    dummy.extend(i)

for i in range(len(dummy)):
    tot += (hm[dummy[i]][0] * (i + 1))

print(tot)
print(dummy)
print(hm)
print(arr)
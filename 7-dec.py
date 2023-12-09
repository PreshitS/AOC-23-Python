with open("input7.txt") as f:
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
        i.sort()
    
for i in range(len(arr[1])):
    arr[1][i] = [len(list(set(arr[1][i]))), arr[1][i]]

for i in range(len(arr[2])):
    arr[2][i] = [len(list(set(arr[2][i]))), arr[2][i]]

for i in range(len(arr)):
    arr[i].sort(reverse = True)

print(arr)

dummy = []
for i in range(len(arr)):
    if i == 0 or i == 3 or i == 4:
        dummy.extend(arr[i])
    else:
        for j in range(len(arr[i])):
            dummy.append(arr[i][j][1])
print()
print(dummy)
tot = 0
for i in range(len(dummy)):
    tot += (hm[dummy[i]][0] * (i + 1))

print(tot)

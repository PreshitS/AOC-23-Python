#first prob
with open("input9.txt") as f:
    lines = f.readlines()

tot = 0

for i in range(len(lines)):
    arr = [lines[i].split()]
    for j in range(len(arr[0])):
        arr[0][j] = int(arr[0][j])
    while arr[-1].count(arr[-1][0]) != len(arr[-1]):
        temp = []
        for j in range(1, len(arr[-1])):
            temp.append(arr[-1][j] - arr[-1][j-1])
        arr.append(temp)
    for j in arr:
        tot += j[-1]

print(tot)

#second prob
with open("input9.txt") as f:
    lines = f.readlines()

tot = 0

for i in range(len(lines)):
    arr = [lines[i].split()]
    for j in range(len(arr[0])):
        arr[0][j] = int(arr[0][j])
    while arr[-1].count(arr[-1][0]) != len(arr[-1]):
        temp = []
        for j in range(1, len(arr[-1])):
            temp.append(arr[-1][j] - arr[-1][j-1])
        arr.append(temp)
    for j in range(len(arr) - 2, -1, -1):
        arr[j][0] = arr[j][0] - arr[j+1][0]
    tot += arr[0][0]

print(tot)
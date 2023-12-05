#first prob
with open("input.txt") as f:
    lines = f.readlines()

tot = 0

for i in range(len(lines)):
    lst = lines[i].split(":")
    arr = lst[1].split("|")
    win = arr[0].split()
    for j in range(len(win)):
        win[j] = int(win[j])
    allc = arr[1].split()
    for j in range(len(allc)):
        allc[j] = int(allc[j])
    count = 0
    print(win, allc)
    for j in range(len(allc)):
        if allc[j] in win:
            count += 1
    print(count)
    tot += (2 ** (count - 1)) if count != 0 else 0
print(tot)

#second prob
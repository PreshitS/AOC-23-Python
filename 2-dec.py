#first prob
with open("input.txt") as f:
    lines = f.readlines()

ans = 0
for i in lines:
    arr = i.split(':')
    arr[1] = arr[1][1:-1]
    arr2 = arr[1].split(';')
    res = []
    for j in arr2:
        arr3 = j.split(",")
        res.extend(arr3)
    k = 0
    while k < len(res):
        lst = res[k].split()
        if lst[1] == "red" and int(lst[0]) > 12:
            break
        elif lst[1] == "green" and int(lst[0]) > 13:
            break
        elif lst[1] == "blue" and int(lst[0]) > 14:
            break
        k += 1
    if k == len(res):
        ans += (lines.index(i) + 1)

print(ans)

#second prob
with open("input.txt") as f:
    lines = f.readlines()

ans = 0
for i in lines:
    arr = i.split(':')
    arr[1] = arr[1][1:-1]
    arr2 = arr[1].split(';')
    res = []
    for j in arr2:
        arr3 = j.split(",")
        res.extend(arr3)
    print(res)
    k = 0
    freq = [1, 1, 1]
    while k < len(res):
        lst = res[k].split()
        if lst[1] == "red" and int(lst[0]) > freq[2]:
            freq[2] = int(lst[0])
        elif lst[1] == "green" and int(lst[0]) > freq[1]:
            freq[1] = int(lst[0])
        elif lst[1] == "blue" and int(lst[0]) > freq[0]:
            freq[0] = int(lst[0])
        k += 1
    ans += (freq[0] * freq[1] * freq[2])

print(ans)
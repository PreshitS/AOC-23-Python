with open("input.txt") as f:
    lines = f.readlines()

dummy = []
i = 0
while i < len(lines):
    arr = []
    while i < len(lines) and lines[i] != '\n':
        arr.append(lines[i]) 
        i += 1
    dummy.append(arr)
    i += 1

seeds = dummy[0][0].split(':')[1]
seeds = seeds.split()

for i in range(len(seeds)):
    seeds[i] = int(seeds[i])

def formatt(arr, dummy, ind):
    arr = []
    arr.extend(dummy[ind][1:])
    for i in range(len(arr)):
        arr[i] = arr[i].split()
        for j in range(3):
            arr[i][j] = int(arr[i][j])
    return arr

seedsoil = formatt([], dummy, 1)
soilfert = formatt([], dummy, 2)
fertwater = formatt([], dummy, 3)
waterlight = formatt([], dummy, 4)
lighttemp = formatt([], dummy, 5)
temphumid = formatt([], dummy, 6)
humidloc = formatt([], dummy, 7)


def final(seeds, arr):
    for i in range(len(seeds)):
        for j in range(len(arr)):
            if seeds[i] >= arr[j][1] and seeds[i] <= arr[j][1] + arr[j][2]:
                seeds[i] = seeds[i] + arr[j][0] - arr[j][1]
                break

final(seeds, seedsoil)
final(seeds, soilfert)
final(seeds, fertwater)
final(seeds, waterlight)
final(seeds, lighttemp)
final(seeds, temphumid)
final(seeds, humidloc)
print(min(seeds))
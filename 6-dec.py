#first_prob
with open("input6.txt") as f:
    lines= f.readlines()

time = lines[0].split(':')[1].split()
distance = lines[1].split(':')[1].split()
for i in range(len(time)):
    time[i] = int(time[i])
    distance[i] = int(distance[i])

tot = 1

for i in range(len(time)):
    count = 0
    for j in range(time[i]+1):
        if (time[i] - j) * j > distance[i]:
            count += 1
    tot *= count

print(tot)

#second prob
with open("input6.txt") as f:
    lines= f.readlines()

time = int("".join(lines[0].split(':')[1].split()))
distance = int("".join(lines[1].split(':')[1].split()))

count = 0
for i in range(time+1):
    if (time - i) * i > distance:
        count += 1

print(count)
f = open("./Day 1/input.txt", "r")

relsum:int = 0
maximum = 0

sums = []

for line in f:
    if line != '\n': relsum+=int(line) 
    else:
        sums.append(relsum)
        relsum =0

sums.sort(reverse=True)



print('A1: '+str(sums[0]))
print('A2: '+str(sums[0]+sums[1]+sums[2]))
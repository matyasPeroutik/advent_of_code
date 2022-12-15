f = open("./Day 3/input.txt", "r")


def calculate_score(char):
    ASCII = ord (char)
    if(ASCII < 97):
        return ASCII - 38
    else: return ASCII - 96

score = 0

for line in f:
    line = line.strip(' \n')

    compartment1 = line[slice(0, len(line)//2)]
    compartment2 = line[slice(len(line)//2, len(line))]
    for char in compartment1:
        if char in compartment2:
            score += calculate_score(char)
            break

print(f'A1: {score}')

f = open("./Day 3/input.txt", "r")

score = 0
index = 0
groups= []

for line in f:
    line = line.strip(' \n')
    if not index%3:
        groups.append([])
    groups[index//3].append(line) 
    index += 1

for group in groups:
    for letter in group[0]:
        if letter in group[1] and letter in group[2]:
            score += calculate_score(letter)
            break

print(f'A2: {score}')


    

    
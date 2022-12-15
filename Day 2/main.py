f = open("./Day 2/input.txt", "r")

score = 0

guide = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

win = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

lose = {
    'C': 'Y',
    'A': 'Z',
    'B': 'X'
}

eq = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'}


for line in f:
    line =line.strip('\n').split(' ')
    if line[1] == win[line[0]]:
        score += 6 + guide[line[1]]

    elif line[1] == eq[line[0]]:
        score += 3 + guide[line[1]]

    else:
        score += guide[line[1]]

print(f'A1: {score}')

score = 0

f = open("./Day 2/input.txt", "r")

for line in f:
    line =line.strip('\n').split(' ')

    if line[1] == 'X':
        score += guide[lose[line[0]]]
    if line[1] == 'Y':
        score += 3+ guide[eq[line[0]]]
    if line[1] == 'Z':
        score += 6+ guide[win[line[0]]]

print(f'A2: {score}')



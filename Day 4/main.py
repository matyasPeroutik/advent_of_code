f = open("./Day 4/input.txt", "r")

score = 0

for line in f:
    line = line.strip(' \n')

    pair = line.split(',')
    pair[0] = pair[0].split('-')
    pair[1] = pair[1].split('-')

    pair1 = int(pair[0][0])
    pair2 = int(pair[0][1])
    pair3 = int(pair[1][0])
    pair4 = int(pair[1][1])

    condition1 = pair1 <= pair3 and pair2 >= pair4
    condition2 = pair1 >= pair3 and pair2 <= pair4

    if condition1 or condition2:
        score += 1
        print('\\/')
        print(pair)

    # for i in range(int(pair[0][0]), int(pair[0][1])+1):
    #     if i >= int(pair[1][0]) and i <= int(pair[1][1]):
    #         state = True
    #     else:
    #         state = False

print(f'A1: {score}')


f = open("./Day 4/input.txt", "r")

score = 0

for line in f:
    line = line.strip(' \n')

    pair = line.split(',')
    pair[0] = pair[0].split('-')
    pair[1] = pair[1].split('-')

    pair1 = int(pair[0][0])
    pair2 = int(pair[0][1])
    pair3 = int(pair[1][0])
    pair4 = int(pair[1][1])

    condition1 = pair1 <= pair3 and pair2 >= pair3
    condition2 = pair2 >= pair4 and pair1 <= pair4
    condition3 = pair1 <= pair3 and pair2 >= pair4
    condition4 = pair1 >= pair3 and pair2 <= pair4
    if condition1 or condition2 or condition3 or condition4:
        score += 1
    else:
        print('\\/')
        print(pair)

print(score)
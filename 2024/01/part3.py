
def count_pots(input):
    p = 0
    for i in range(0, len(input), 3):
        if input[i] == 'B':
            p += 1
        if input[i+1] == 'B':
            p += 1
        if input[i+2] == 'B':
            p += 1
        if input[i] == 'C':
            p += 3
        if input[i+1] == 'C':
            p += 3
        if input[i+2] == 'C':
            p += 3
        if input[i] == 'D':
            p += 5
        if input[i+1] == 'D':
            p += 5
        if input[i+2] == 'D':
            p += 5
        xs = input[i:i+3].count('x')    
        if xs == 1:
            p += 2
        elif xs == 0:
            p += 6
    # print(input + ' -> ' + str(p))
    return p

assert(count_pots('xBxAAABCDxCC') == 30)

with open('2024/input3.txt') as fp:
    for line in fp:
        print(count_pots(line.strip()))


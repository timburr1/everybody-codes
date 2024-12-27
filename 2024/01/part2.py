
def count_pots(input):
    p = 0
    for i in range(0, len(input), 2):
        if input[i] == 'B':
            p += 1
        if input[i+1] == 'B':
            p += 1
        if input[i] == 'C':
            p += 3
        if input[i+1] == 'C':
            p += 3
        if input[i] == 'D':
            p += 5
        if input[i+1] == 'D':
            p += 5
        if input[i] != 'x' and input[i+1] != 'x':
            p += 2
    # print(input + ' -> ' + str(p))
    return p

assert(count_pots('AxBCDDCAxD') == 28)

with open('2024/input2.txt') as fp:
    for line in fp:
        print(count_pots(line.strip()))


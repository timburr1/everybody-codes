
def count_pots(input):
    p = 0
    for i in range(len(input)):
        if input[i] == 'B':
            p += 1
        elif input[i] == 'C':
            p += 3
    return p

with open('2024/input.txt') as fp:
    for line in fp:
        print(count_pots(line.strip()))

assert(count_pots('ABBAC') == 5)
import sys
from math import ceil, sqrt

input = int(sys.stdin.readline())


# Part 1
def position(n):
    k = ceil((sqrt(n) - 1) / 2)
    t = 2 * k + 1
    m = pow(t, 2)

    t -= 1

    if n >= m - t:
        return [k - (m - n), -k]

    m -= t

    if n >= m - t:
        return [-k, -k + (m - n)]

    m -= t

    if n >= m - t:
        return [-k + (m - n), k]

    return [k, k - (m - n - t)]


distance = sum(map(abs, position(input)))
print('Part 1:', distance)

# Part 2
i = 0
j = 0
d = 'r'
memory = {(i, j): 1}
while True:
    if d == 'r':
        i += 1
        if (i, j + 1) not in memory:
            d = 'u'
    elif d == 'u':
        j += 1
        if (i - 1, j) not in memory:
            d = 'l'
    elif d == 'l':
        i -= 1
        if (i, j - 1) not in memory:
            d = 'b'
    elif d == 'b':
        j -= 1
        if (i + 1, j) not in memory:
            d = 'r'

    res = 0
    for n in range(-1, 2):
        for m in range(-1, 2):
            pos = (i + n, j + m)
            if pos in memory:
                res += memory[pos]
    memory[(i, j)] = res

    if res > input:
        break
print('Part 2:', res)
